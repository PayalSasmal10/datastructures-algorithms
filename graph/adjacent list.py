"""
This is a undirected graph
A---C---E
|   |   |
B---D---|
"""

class createGraph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph_dict = {}

        # create blank values for all the vertices
        for node in self.vertices:
            self.graph_dict[node] = []
    def add_edges(self, vertices, edges):
        self.graph_dict[vertices].append(edges)
        self.graph_dict[edges].append(vertices)

    # no of vertices connected with each other like A has 2 degree B and C
    def degree(self,vertices):
        return len(self.graph_dict[vertices])

    def printGraph(self):
        for node in self.vertices:
            print(node, "->", self.graph_dict[node])


vertices = ["A", "B", "C", "D", "E"]
edges = [
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("C","D"),
    ("C","E"),
    ("D","E"),
    
    ]
adj_list = createGraph(vertices)
adj_list.printGraph()
for v,e in edges:
    adj_list.add_edges(v,e)
adj_list.printGraph()

print(f"degree of c is : ", adj_list.degree("C"))





