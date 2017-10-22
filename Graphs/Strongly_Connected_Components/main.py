from Graphs.DFS.main import DFSGraph
from Stacks.stack1 import Stack

stk = Stack()
g = DFSGraph()

for i in range(5):
    g.addVertex(i)

g.addEdge(1, 0, 1)
g.addEdge(0, 2, 1)
g.addEdge(2, 1, 1)
g.addEdge(0, 3, 1)
g.addEdge(3, 4, 1)

# g.addEdge(0, 1, 5)
# g.addEdge(0, 5, 2)
# g.addEdge(1, 2, 4)
# g.addEdge(2, 3, 9)
# g.addEdge(3, 4, 7)
# g.addEdge(3, 5, 3)
# g.addEdge(4, 0, 1)
# g.addEdge(5, 4, 8)
# g.addEdge(5, 2, 1)

# STEP 1: Run dfs on the graph to calculate finish times for the vertices
g.dfs()

# STEP 2: Transpose the Graph
g.transpose_graph()

# STEP 3: Reverse the vertList for the graph and store it in a list
x = reversed(sorted(g.vertList, key=lambda x: g.vertList[x].finish))

# STEP 4: Push each element into a stack
for v in x:
    stk.push(g.vertList[v])

# STEP 5: Reset color of the vertices to white and predecessor to -1
for aVertex in g:
    aVertex.setColor('white')
    aVertex.setPredecessor(-1)

# STEP 6: Call dfs on each vertex in the stack until the stack is empty
print("The strongly connected components are: ")
while not stk.isEmpty():
    v = stk.pop()
    if v.getColor() == 'white':
        g.dfs_visit(v, True)
        print("-----------------")