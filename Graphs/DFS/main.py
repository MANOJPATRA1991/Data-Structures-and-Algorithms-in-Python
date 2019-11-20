from Graphs.Graph.main import Graph


class DFSGraph(Graph):
    """
    A derived class from Graph base class
    Args:
        time(int): To keep track of when a Vertex is discovered
                and when it is completely explored
    """

    #
    # Run time for dfs => O(V+E)
    #
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        """
        Starts the depth first search
        """
        # Run time => O(V)
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPredecessor(-1)
        # Run time => O(V)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfs_visit(aVertex)

    def dfs_visit(self, start_vertex, p=False):
        """
        Args:
            start_vertex(Vertex): The starting node for DFS
            p(bool): Print value if True (used in case of
                    finding strongly connected components)
        """
        #
        # as the loop will execute a max of once for every edge
        #
        # Recursive call occurs only if color of vertex is white
        #
        # CONCLUSION:
        #     all the children of a particular node in the
        #     depth first tree have a later discovery time
        #     and an earlier finish time than their parent
        start_vertex.setColor('gray') # In the process of being visited
        if p:
            print(start_vertex.id)
        start_vertex.setDiscovery(self.time)
        self.time += 1
        # Start visiting all vertices
        # connected to start_vertex
        # Run-time => O(E)
        for v in start_vertex.getConnections():
            if v.getColor() == 'white':
                v.setPredecessor(start_vertex)
                if p:
                    self.dfs_visit(v, True)
                else:
                    self.dfs_visit(v)
        # Mark as visited
        start_vertex.setColor('black')
        self.time += 1
        start_vertex.setFinish(self.time)
