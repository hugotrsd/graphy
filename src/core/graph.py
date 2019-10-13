import json
from collections import namedtuple


class Graph:
    def __init__(self):
        self.title = "untitled"
        
        self.directed = False
        self.vertex_weighted = False
        self.edge_weighted = False

        self.vertices = []
        self.vertices_weights = []

        self.edges = []
        self.edges_weights = []

    def saveToFile(self, filename):
        filename = filename.replace(".json", "")  # Prevent doubled extension
        with open(f"{filename}.json", "w") as file:
            json.dump(self.__dict__, file, indent=2)

    @staticmethod
    def loadFromFile(filename: str):  # -> Graph
        def dictToObj(data: dict):
            g = Graph()
            g.__dict__ = data.copy()  # That's crazy cool actually
            return g

        if not ".json" in filename:
            filename += ".json"
        with open(filename, "r") as file:
            graph = json.load(file, object_hook=dictToObj)
        return graph

    def __eq__(self, obj):
        if not isinstance(obj, Graph):
            raise NotImplementedError

        if self is obj:
            return True

        return self.__dict__ == obj.__dict__

    def __ne__(self, obj):
        return not self == obj

    def __str__(self):
        return f"{super().__str__()}: {str(self.__dict__)}"
