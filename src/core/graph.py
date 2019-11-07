from copy import deepcopy

import bisect
import logging
import json


class Graph:
    def __init__(self):
        self._title = "untitled"

        self._vertices = [False]  # (isDirected: bool, adjacency_list...)
        self._vertices_names = {}  # "name": index_int
        self._vertices_weights = [False]  # (isVertexWeighted: bool, weight: float...)
        self._edges_weights = [False, []]  # (isEdgeWeighted: bool, matrix_float(vertexStart: int, vertexEnd: int))

    def title(self):
        return self._title

    def setTitle(self, title: str):
        self._title = title

    def addVertex(self, vertex: str):
        if vertex in self._vertices_names:
            raise ValueError(f"Vertex {vertex} already exist")
        self._vertices.append([])
        self._vertices_names[vertex] = len(self._vertices) - 1

    def addVertices(self, vertexList: list):
        for v in vertexList:
            self.addVertex(v)

    def removeVertex(self, vertex: str):
        try:
            v = self._vertices_names[vertex]
        except KeyError as e:
            raise RuntimeError(f"Vertex {e} does not exist") from e

        for adj in range(1, len(self._vertices)):
            if adj != v:
                listLength = len(self._vertices[adj])
                for i in range(listLength):
                    ri = listLength - 1 - i
                    if self._vertices[adj][ri] > v:
                        self._vertices[adj][ri] -= 1
                        
                    elif self._vertices[adj][ri] == v:
                        del self._vertices[adj][ri]

        del self._vertices[v]

    def addEdge(self, vertexStart: str, vertexEnd: str):
        try:
            vs = self._vertices_names[vertexStart]
            ve = self._vertices_names[vertexEnd]
        except KeyError as e:
            raise RuntimeError(f"Vertex {e} does not exist") from e

        bisect.insort(self._vertices[vs], ve)
        if not self._vertices[0]:
            bisect.insort(self._vertices[ve], vs)

    def removeEdge(self, vertexStart: str, vertexEnd: str):
        try:
            vs = self._vertices_names[vertexStart]
            ve = self._vertices_names[vertexEnd]
        except KeyError as e:
            raise RuntimeError(f"Vertex {e} does not exist") from e

        try:
            self._vertices[vs].remove(ve)
        except ValueError as e:
            logging.error(f"Attempted to remove non-existant edge {vertexStart} -> {vertexEnd}")
            return

        try:
            if not self._vertices[0]:
                self._vertices[ve].remove(vs)
        except ValueError as e:
            logging.error(f"Attempted to remove non-existant edge {vertexEnd} -> {vertexStart}")

    def vertices(self) -> list:
        return self._vertices[1:]

    def verticesWeights(self) -> list:
        if not self._vertices_weights:
            raise RuntimeError("This graph is not vertex weighted")
        return self._vertices_weights[1:]

    def edges(self) -> list:
        L = []
        for v in range(1, len(self._vertices)):
            for n in self._vertices[v]:
                if v > n and not self._vertices[0]:
                    continue
                L.append((v, n))
        return L

    def edgesWeights(self) -> list:
        if not self._edges_weights:
            raise RuntimeError("This graph is not edge weighted")
        return deepcopy(self._edges_weights[1])

    def isDirected(self) -> bool:
        return self._vertices[0]

    def saveToFile(self, fileName: str):
        fileName = fileName.replace(".json", "")  # Prevent double extension
        with open(f"{fileName}.json", "w") as file:
            json.dump(self.__dict__, file, indent=4)

    @staticmethod
    def loadFromFile(fileName: str):  # -> Graph
        if not ".json" in fileName:
            fileName += ".json"
        with open(fileName, "r") as file:
            graphDict = json.load(file)

        g = Graph()
        g.__dict__ = graphDict.copy()
        return g

    def __eq__(self, obj):
        if not isinstance(obj, Graph):
            raise NotImplementedError

        if self is obj:
            return True

        return self.__dict__ == obj.__dict__

    def __ne__(self, obj):
        return not self == obj

    def __str__(self):
        return f"{super().__str__()}: {self.__dict__}"
