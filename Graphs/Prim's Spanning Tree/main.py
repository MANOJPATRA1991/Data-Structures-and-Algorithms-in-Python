import sys

from Graphs.Graph.main import Graph
from Graphs.Priority_Queue_DFS.main import PriorityQueue
from Graphs.Vertex.main import Vertex


def dijkshtra(aGraph, start):
    """
    Prim's Spanning Tree Algorithm.
    Args:
        aGraph(Graph)A
        start(Vertex)
    """
    # Combined run time ~= O((E + V)log(V))
    pq = PriorityQueue()
    # O(V)
    for v in aGraph:
        v.setDistance(sys.maxsize)
    start.setDistance(0)
    # O(V)
    pq.build_heap([(v.getDistance(), v) for v in aGraph])
    # O(V)
    while not pq.is_empty():
        # O(logV)
        current_vert = pq.del_min()
        # O(E)
        for next_vert in current_vert.getConnections():
            new_cost = current_vert.getDistance() + current_vert.getWeight(next_vert)
            if next_vert in pq and new_cost < next_vert.getDistance():
                next_vert.setDistance(new_cost)
                next_vert.setPredecessor(current_vert)
                print(next_vert.id, " | ", next_vert.getDistance(), " | ", next_vert.getPredecessor())
                # O(logV)
                pq.decrease_key(next_vert, new_cost)


gg = Graph()

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')
g = Vertex('g')

gg.addVertex(a.id)
gg.addVertex(b.id)
gg.addVertex(c.id)
gg.addVertex(d.id)
gg.addVertex(e.id)
gg.addVertex(f.id)
gg.addVertex(g.id)

gg.addEdge(a.id, b.id, 2)
gg.addEdge(a.id, c.id, 3)
gg.addEdge(b.id, a.id, 2)
gg.addEdge(b.id, c.id, 1)
gg.addEdge(b.id, d.id, 1)
gg.addEdge(c.id, a.id, 3)
gg.addEdge(c.id, b.id, 1)
gg.addEdge(c.id, f.id, 5)
gg.addEdge(d.id, b.id, 1)
gg.addEdge(d.id, e.id, 1)
gg.addEdge(e.id, b.id, 4)
gg.addEdge(e.id, d.id, 1)
gg.addEdge(e.id, f.id, 1)
gg.addEdge(e.id, f.id, 1)
gg.addEdge(f.id, c.id, 5)
gg.addEdge(f.id, g.id, 1)
gg.addEdge(g.id, f.id, 1)

dijkshtra(gg, gg.getVertex(a.id))
