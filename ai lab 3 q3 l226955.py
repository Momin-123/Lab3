class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def get_neighbors(self, node):
        return self.adj_list[node]

    def heuristic(self, node):
        H = {
            'The': 4,
            'Cat': 3,
            'Dog': 3,
            'runs': 2,
            'fast': 1
        }
        return H[node]

    def a_star(self, start, goal):
        open_set = set([start])
        closed_set = set([])

        cost = {}
        cost[start] = 0

        parents = {}
        parents[start] = start

        while len(open_set) > 0:
            current = None

            for node in open_set:
                if current is None or cost[node] + self.heuristic(node) < cost[current] + self.heuristic(current):
                    current = node

            if current is None:
                print("Path does not exist!")
                return None

            if current == goal:
                path = []

                while parents[current] != current:
                    path.append(current)
                    current = parents[current]

                path.append(start)
                path.reverse()

                print('Path found:', ' -> '.join(path))
                print('Total Cost:', cost[goal])
                return path

            for (neighbor, edge_cost) in self.get_neighbors(current):
                if neighbor not in open_set and neighbor not in closed_set:
                    open_set.add(neighbor)
                    parents[neighbor] = current
                    cost[neighbor] = cost[current] + edge_cost

                else:
                    if cost[neighbor] > cost[current] + edge_cost:
                        cost[neighbor] = cost[current] + edge_cost
                        parents[neighbor] = current

                        if neighbor in closed_set:
                            closed_set.remove(neighbor)
                            open_set.add(neighbor)

            open_set.remove(current)
            closed_set.add(current)

        print("Path does not exist!")
        return None


adj_list = {
    'The': [('Cat', 2), ('Dog', 3)],
    'Cat': [('runs', 1)],
    'Dog': [('runs', 2)],
    'runs': [('fast', 2)],
    'fast': []
}

graph = Graph(adj_list)
graph.a_star('The', 'fast')
