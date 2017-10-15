from Graphs.Graph.main import Graph
from Queues.queue import Queue

import os

def buildGraph(wordFile):
    """
    Build a Graph from the wordfile
    Args:
        wordFile(file): File to read
    Returns:
        Graph: A Graph with vertices and edges created from the word file
    """
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create bucket of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
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
    """
    A BFS proceeds by finding all the vertices that are a distance 'k' 
    from the starting vertex 's' before it finds any vertices that are 
    a distance 'k+1'
    
    A 'white' vertex is an undiscovered vertex.
    
    A 'gray' vertex has some white vertices adjacent to it, i.e., there
    are still additional vertices to explore.
    
    A 'black' vertex has no white vertices adjacent to it, i.e., it is 
    completely explored.
    
    Args:
        g(Graph): Graph on which BFS is performed
        start(Vertex): The starting vertex of the Graph
    """
    start.setDistance(0)
    start.setPredecessor(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    # do until all the vertices in the graph 
    # have color 'black', i.e., completely explored
    while vertQueue.size() > 0:     # while queue is not empty
    #
    # while loop is executed at most once for each vertex in the Graph => O(V)
    #
        currentVert = vertQueue.dequeue()      # remove first element
        for nbr in currentVert.getConnections():       # get connected vertices for  currentVert
        #
        # for loop is executed once for each edge in the Graph after a Vertex is dequeued at most once => O(E)
        #
            if nbr.getColor() == "white":      # if unexplored
                nbr.setColor("gray")       # set color of vertex to gray    
                nbr.setDistance(currentVert.getDistance() + 1)      # increment distance
                nbr.setPredecessor(currentVert)     # set predecessor to currentVert
                vertQueue.enqueue(nbr)      # enqueue neighbor to queue
        currentVert.setColor("black")       # set current vertex color to black as it is now completely explored
    #
    # Combining the two loops => O(V + E)
    #
    # Following the links from the starting node to the goal node is O(V) in worst-case if the graph was a single long chain.
    # Normally it would be a fraction of O(V) still = O(V)

def traverse(y):
    """
    Follow the predecessor links to print the original word
    FOOL -------------- SAGE
    Print FOOL
    """
    x = y
    while x.getPredecessor():
        print(x.getId())
        x = x.getPredecessor()
    print(x.getId())


gg = buildGraph(os.path.abspath("H:/Data_Structures_and_Algorithms_in_Python/Graphs/wordLadder.txt"))
bfs(gg, gg.getVertex('fool'))
traverse(gg.getVertex('sage'))
