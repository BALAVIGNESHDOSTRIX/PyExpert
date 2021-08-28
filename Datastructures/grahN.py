class Graph:
    def __init__(self, routes):
        self.start_end_edges = {}
        for start, end in routes:
            self.start_end_edges.setdefault(start, []).append(end)
    
    @property
    def getEdges(self):
        return self.start_end_edges

    def get_start_end_paths(self, start=None, end=None, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.getEdges:
            return 

        all_s_e_paths = []
        for node in self.getEdges.get(start):
            if node not in path:
                newpaths = self.get_start_end_paths(node, end=end, path=path)
                for newp in newpaths:
                    all_s_e_paths.append(newp)
        return all_s_e_paths



if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    grp = Graph(routes=routes)
    start = "Mumbai"
    end = "New York"
    print(grp.get_start_end_paths(start=start, end=end))

    