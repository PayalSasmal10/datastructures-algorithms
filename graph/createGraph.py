class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = {}

        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("Graph dict", self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    # based on minimum no of stops
    def get_shortest_paths(self, start, end, path=[]):
        path = path + [start]
        print("first path", path)
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_paths(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path        



if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),

    ]

    route_graph = Graph(routes)
    start = "Mumbai"
    end = "New York"

    print(f"Path from {start} to {end} is : ", route_graph.get_paths(start,end))

    print(f"shortest path to reach from {start} to {end} are : ", route_graph.get_shortest_paths(start,end))