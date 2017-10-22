from Graphs.DFS.main import DFSGraph
from Stacks.stack1 import Stack

stk = Stack()
gg = DFSGraph()

#
# STIRRING A BATCH OF PANCAKES
#
a = 'Pour 3/4 cup milk'
b = 'Break 1 egg'
c = 'Pour 1 Tbl Oil'
d = 'Take 1 cup pancake mix'
e = 'Heat the syrup'
f = 'Heat the griddle'
g = 'Pour 1/4 cup'
h = 'Turn over when pancake starts to bubble'
i = 'Eat'

gg.addVertex(a)
gg.addVertex(b)
gg.addVertex(c)
gg.addVertex(d)
gg.addVertex(e)
gg.addVertex(f)
gg.addVertex(g)
gg.addVertex(h)
gg.addVertex(i)

gg.addEdge(a, d)
gg.addEdge(b, d)
gg.addEdge(c, d)
gg.addEdge(d, g)
gg.addEdge(d, e)
gg.addEdge(e, i)
gg.addEdge(f, g)
gg.addEdge(g, h)
gg.addEdge(h, i)

# STEP 1: Perform Depth First Search on the Graph
gg.dfs()

# STEP 2: Print the vertices in reverse order of finish time
#       (The time taken to explore a vertex)
for (i,v) in enumerate(reversed(sorted(gg.vertList, key=lambda x: gg.vertList[x].finish))):
    print("Step-{0}: {1}".format(i+1, gg.vertList[v].id))
