class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = "white"
        self.predecessor = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDistance(self, n):
        self.distance = n

    def getDistance(self):
        return self.distance

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setPredecessor(self, v):
        self.predecessor = v

    def getPredecessor(self):
        return self.predecessor
