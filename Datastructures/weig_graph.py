class Wgraph:
    def __init__(self, edges):
        self.weight_edges = {}
        self.km_distance = {}
        for start, end, km in edges:
            self.km_distance[(start, end)] = km
            self.weight_edges.setdefault(start, []).append(end)

    @property
    def getEdges(self):
        return self.weight_edges

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

    def calculate_path_min_distance(self, all_path):
        path_v = []
        sort_km = 0
        for path_l in all_path:
            value = 0
            for x in range(1, len(path_l) - 1):
                st = path_l[x-1]
                end = path_l[x]
                value += self.km_distance.get((st,end))
            path_v.append(value)
        if path_v:
            sort_km = min(path_v)
        return (sort_km, all_path[path_v.index(sort_km)])

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris", 400),
        ("Mumbai", "Dubai", 1200),
        ("Paris", "Dubai", 300),
        ("Paris", "New York",700),
        ("Dubai", "New York", 600),
        ("New York", "Toronto", 1200),
    ]
    wgrh = Wgraph(edges=routes)
    start = "Mumbai"
    end = "New York"
    all_paths = wgrh.get_start_end_paths(start=start, end=end)
    print("All Paths: ", all_paths)
    print("")
    srt_km, min_path = wgrh.calculate_path_min_distance(all_path=[['Mumbai', 'Paris', 'Dubai', 'New York']])
    print("Sortest Path: ", min_path, "Total Km: ", srt_km)