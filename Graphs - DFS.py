class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    """def getVertices(self):
        return list(self.gdict.keys())

    # Add the vertex as a key
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def edges(self):
        return self.findedges()
# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename"""

#DFS Code
    def dfs(self, start, visited=None):
        visited = []
        node_stack = []
        output = []
        #create 3 lists: (1)The stack (2)List to keep track of visited nodes (3)list to store our output
        vert = start
        node_stack.append(vert)
        visited.append(vert)
        #for all nodes linked to the start node we can run a dfs using the code below
        while len(node_stack) > 0:
            vert = node_stack.pop()
            visited.append(vert)
            output.append(vert)
            for adjvert in self.gdict[vert]:
                if adjvert in visited:
                    None
                else:
                    node_stack.append(adjvert)
                    visited.append(adjvert)

#This check for any nodes that are not directly or indirectly linked to the start node and runs algorithm through them
        #by checking all of the nodes listed in the graph and verifying if they have been visited
        for key in self.gdict:
            if key not in visited:
                vert = key
                node_stack.append(vert)
                visited.append(vert)
                while len(node_stack) > 0:
                    vert = node_stack.pop()
                    visited.append(vert)
                    output.append(vert)
                    for adjvert in self.gdict[vert]:
                        if adjvert in visited:
                            None
                        else:
                            node_stack.append(adjvert)
                            visited.append(adjvert)
        return output

graph_elements = {}

#User Interface allowing userto enter their own unique graph
number_of_vertices = int(input("How many Nodes does the graph have?: "))
count = 0
while count < number_of_vertices:
    vertex = input("Add a vertex: ")
    number_of_adjvertices = int(input("How many  adjacent Nodes does '" + vertex + "' have?: "))
    if number_of_adjvertices > number_of_vertices:
        print("Check graph and try again")
        exit()
    adjcount = 0
    list_of_adj = []
    while adjcount < number_of_adjvertices:
        adjvertex = input("Add a vertex adjacent: ")
        list_of_adj.append(adjvertex)
        adjcount += 1
    graph_elements[vertex] = list_of_adj
    count +=1


g = graph(graph_elements)

start_node = input("Which node do you want to start with? ")

print(g.dfs(start_node))

"""print(graph_elements)
print(g.getVertices())
print(g.edges())"""