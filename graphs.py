class Vertex(object):
    def __init__(self,key):
        """ Represents each Vertex in a graph.
        Uses dictionary to track vertices to which each vertex is connected to
        including the weight of its edge"""
        self.id = key
        self.connectTo = {}

    def neighbor(self, nbr, weight=0):
        # add neighbor to connectTo dictionary with weight
        self.connectTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectTo])

    def getConnections(self):
        # get all connecting vertices

        return self.connectTo.keys()

    def getId(self):
        # get Id

        return self.id

    def getWeight(self,nbr):
        # get weight with nbr as key

        return self.connectTo[nbr]


class Graph(object):
    """Dictionary that maps vertex names to vertex objects.
    Can also add a vertice to a graph.
    Connects one vertices to another."""

    def __init__(self):
        self.vertList={}
        self.numVertices = 0

    def addVertex(self,key):
        # add to vertex number
        self.numVertices = self.numVertices + 1

        # instantiate a newvertex
        newVertex = Vertex(key)

        # add key and newVertex in vertlist
        self.vertlist[key] = newVertex
        return newVertex

    def getVertex(self,n):
        # get vertex n if it exists in vertList
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        # if f not existing in list add vertex f
        if f not in self.vertList:
            nv = self.addVertex(f)

        # if t not existing in vertlist add vertex t
        if t not in self.vertList:
            nv = self.addVertex(t)

        # add neighbor t to f with wieght calling addNeighbor function in Vertex class
        self.vertList[f]. addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())