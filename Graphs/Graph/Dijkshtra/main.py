from Graphs.Graph.main import Graph
from Graphs.Vertex.main import Vertex
from Graphs.Graph.Priority_Queue_DFS.main import PriorityQueue
import sys


def dijkshtra(aGraph, start):
    """
    Dijkstra’s algorithm works only when the weights are all positive.
    Args:
        aGraph(Graph)
        start(Vertex)
    """
    # Combined run time ~= O((E + V)log(V))
    pq = PriorityQueue()
    start.setDistance(0)
    # O(V)
    pq.build_heap([(v.getDistance(), v) for v in aGraph])
    # O(V)
    while not pq.is_empty():
        # O(logV)
        current_vert = pq.del_min()
        # O(E)
        for next_vert in current_vert.getConnections():
            new_dist = current_vert.getDistance() + current_vert.getWeight(next_vert)
            if new_dist < next_vert.getDistance():
                next_vert.setDistance(new_dist)
                next_vert.setPredecessor(current_vert)
                print(next_vert.id, " | ", next_vert.getDistance(), " | ", next_vert.getPredecessor())
                # O(logV)
                pq.decrease_key(next_vert, new_dist)


g = Graph()

a = Vertex(111)
b = Vertex(112)
c = Vertex(113)
d = Vertex(114)
e = Vertex(115)
f = Vertex(116)

g.addVertex(a.id)
g.getVertex(a.id).setDistance(sys.maxsize)
g.addVertex(b.id)
g.getVertex(b.id).setDistance(sys.maxsize)
g.addVertex(c.id)
g.getVertex(c.id).setDistance(sys.maxsize)
g.addVertex(d.id)
g.getVertex(d.id).setDistance(sys.maxsize)
g.addVertex(e.id)
g.getVertex(e.id).setDistance(sys.maxsize)
g.addVertex(f.id)
g.getVertex(f.id).setDistance(sys.maxsize)

g.addEdge(a.id, b.id, 2)
g.addEdge(a.id, c.id, 5)
g.addEdge(a.id, d.id, 1)
g.addEdge(b.id, a.id, 2)
g.addEdge(b.id, c.id, 3)
g.addEdge(b.id, d.id, 2)
g.addEdge(c.id, a.id, 5)
g.addEdge(c.id, b.id, 3)
g.addEdge(c.id, d.id, 3)
g.addEdge(c.id, e.id, 1)
g.addEdge(c.id, f.id, 5)
g.addEdge(d.id, a.id, 1)
g.addEdge(d.id, b.id, 2)
g.addEdge(d.id, c.id, 3)
g.addEdge(d.id, e.id, 1)
g.addEdge(e.id, d.id, 1)
g.addEdge(e.id, c.id, 1)
g.addEdge(e.id, f.id, 1)
g.addEdge(f.id, c.id, 5)
g.addEdge(f.id, e.id, 1)

dijkshtra(g, g.getVertex(a.id))
