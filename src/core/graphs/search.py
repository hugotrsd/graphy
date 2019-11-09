from core.graphs.graph import Graph
from collections import deque


class SearchEventType:
    SEARCH_START = 1
    SEARCH_END = 2
    TREE_DISCOVER_START = 3
    TREE_DISCOVER_END = 4
    VERTEX_DISCOVER_START = 5
    VERTEX_DISCOVER_END = 6
    VERTEX_REDISCOVER_BACK_EDGE = 7
    VERTEX_REDISCOVER_FORWARD_EDGE = 8
    VERTEX_REDISCOVER_CROSS_EDGE = 9


class SearchEvent:
    def __init__(self, searchEventType, vertex: int = None):
        self.type = searchEventType
        self.vertex = vertex


def DFS(graph: Graph) -> list:
    discovered = [0 for i in range(len(graph._vertices))]
    ancestors = [0 for i in range(len(graph._vertices))]
    eventList = []

    def isAncestor(ancestor: int, child: int):
        while ancestors[child] != child:
            child = ancestors[child]
            if child == ancestor:
                return True
        return False

    def DFSrec(vertex: int):
        for i in graph._vertices[vertex]:
            if discovered[i] == 0:
                eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_START, i))
                discovered[i] = 1
                
                if ancestors[i] == 0:
                    ancestors[i] = vertex

                DFSrec(i)
                discovered[i] = 2
                eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_END, i))

            elif discovered[i] == 1:
                eventList.append(SearchEvent(SearchEventType.VERTEX_REDISCOVER_BACK_EDGE, i))

            elif discovered[i] == 2:
                if isAncestor(i, vertex):
                    eventList.append(SearchEvent(SearchEventType.VERTEX_REDISCOVER_FORWARD_EDGE, i))
                else:
                    eventList.append(SearchEvent(SearchEventType.VERTEX_REDISCOVER_CROSS_EDGE))

    eventList.append(SearchEvent(SearchEventType.SEARCH_START))

    for i in range(1, len(graph._vertices)):
        if discovered[i] == 0:
            eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_START, i))
            discovered[i] = 1
            ancestors[i] = i
            DFSrec(i)
            discovered[i] = 2
            eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_END, i))

    eventList.append(SearchEvent(SearchEventType.SEARCH_END))
    return eventList


def BFS(graph: Graph):
    discovered = [0 for i in range(len(graph._vertices))]
    fifo = deque()
    eventList = []

    eventList.append(SearchEvent(SearchEventType.SEARCH_START))

    for i in range(1, len(graph._vertices)):
        if discovered[i] == 0:
            fifo.append(i)
            eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_START, i))
            discovered[i] = 1

            while fifo:
                current = fifo.popleft()
                eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_END, current))
                discovered[current] = 1

                for v in graph._vertices[current]:
                    if discovered[v] == 0:
                        fifo.append(v)
                        eventList.append(SearchEvent(SearchEventType.VERTEX_DISCOVER_START, v))
                        discovered[v] = 1
                    
                    elif discovered[v] == 1:
                        eventList.append(SearchEvent(SearchEventType.VERTEX_REDISCOVER_BACK_EDGE))

                    elif discovered[v] == 2:
                        eventList.append(SearchEvent(SearchEventType.VERTEX_REDISCOVER_CROSS_EDGE))

            for i in range(len(discovered)):
                if discovered[i] == 1:
                    discovered[i] = 2
    
    eventList.append(SearchEvent(SearchEventType.SEARCH_END))
    return eventList
