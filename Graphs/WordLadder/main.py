from Graphs.Graph.main import Graph
from Queues.queue import Queue

import os


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')

    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    # print(g)
    # for v in g:
    #     for w in v.getConnections():
    #         print("( %s, %s )" % (v.getId(), w.getId()))

    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPredecessor(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPredecessor(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor("black")


def traverse(y):
    x = y
    while x.getPredecessor():
        print(x.getId())
        x = x.getPredecessor()
    print(x.getId())


gg = buildGraph(os.path.abspath("H:/Data_Structures_and_Algorithms_in_Python/Graphs/wordLadder.txt"))
bfs(gg, gg.getVertex('fool'))
traverse(gg.getVertex('sage'))