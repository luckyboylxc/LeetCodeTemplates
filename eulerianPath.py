class EulerianPathDirectedEdgesAdjacencyList:
    def __init__(self, graph):
        if graph is None:
            raise ValueError("Graph cannot be None")
        self.n = len(graph)
        self.graph = graph
        self.path = []

    def get_eulerian_path(self):
        self.setUp()

        if not self.graph_has_eulerian_path():
            return None
        
        self.dfs(self.find_start_node())

        if len(self.path) != self.edge_count + 1:
            return None

        return self.path[::-1]

    def setUp(self):
        self.in_deg = [0] * self.n
        self.out_deg = [0] * self.n
        self.edge_count = 0

        for from_node in range(self.n):
            for to_node in self.graph[from_node]:
                self.in_deg[to_node] += 1
                self.out_deg[from_node] += 1
                self.edge_count += 1

    def graph_has_eulerian_path(self):
        if self.edge_count == 0:
            return False

        start_nodes = 0
        end_nodes = 0
        for i in range(self.n):
            if self.out_deg[i] - self.in_deg[i] > 1 or self.in_deg[i] - self.out_deg[i] > 1:
                return False
            elif self.out_deg[i] - self.in_deg[i] == 1:
                start_nodes += 1
            elif self.in_deg[i] - self.out_deg[i] == 1:
                end_nodes += 1

        return (end_nodes == 0 and start_nodes == 0) or (end_nodes == 1 and start_nodes == 1)

    def find_start_node(self):
        start = 0
        for i in range(self.n):
            if self.out_deg[i] - self.in_deg[i] == 1:
                return i
            if self.out_deg[i] > 0:
                start = i
        return start

    def dfs(self, at):
        while self.out_deg[at] != 0:
            next_node = self.graph[at][-1]
            self.graph[at].pop()
            self.out_deg[at] -= 1
            self.dfs(next_node)
        self.path.append(at)

def initialize_empty_graph(n):
    return [[] for _ in range(n)]

def add_directed_edge(graph, from_node, to_node):
    graph[from_node].append(to_node)

def main():
    example_from_slides()
    small_example()

def example_from_slides():
    n = 7
    graph = initialize_empty_graph(n)

    add_directed_edge(graph, 1, 2)
    add_directed_edge(graph, 1, 3)
    add_directed_edge(graph, 2, 2)
    add_directed_edge(graph, 2, 4)
    add_directed_edge(graph, 2, 4)
    add_directed_edge(graph, 3, 1)
    add_directed_edge(graph, 3, 2)
    add_directed_edge(graph, 3, 5)
    add_directed_edge(graph, 4, 3)
    add_directed_edge(graph, 4, 6)
    add_directed_edge(graph, 5, 6)
    add_directed_edge(graph, 6, 3)

    solver = EulerianPathDirectedEdgesAdjacencyList(graph)
    print(solver.get_eulerian_path())

def small_example():
    n = 5
    graph = initialize_empty_graph(n)

    add_directed_edge(graph, 0, 1)
    add_directed_edge(graph, 1, 2)
    add_directed_edge(graph, 1, 4)
    add_directed_edge(graph, 1, 3)
    add_directed_edge(graph, 2, 1)
    add_directed_edge(graph, 4, 1)

    solver = EulerianPathDirectedEdgesAdjacencyList(graph)
    print(solver.get_eulerian_path())

if __name__ == "__main__":
    main()