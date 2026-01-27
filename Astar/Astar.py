def a_star(start, goal, graph, heuristic):
    OPEN = [start]
    CLOSED = []

    g = {}
    parent = {}

    g[start] = 0
    parent[start] = None

    while OPEN:

        current = OPEN[0]
        for node in OPEN:
            if g[node] + heuristic[node] < g[current] + heuristic[current]:
                current = node

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()

            min_cost = g[goal]   # ⭐ minimum cost found
            return path, min_cost

        OPEN.remove(current)
        CLOSED.append(current)

        for neighbour, cost in graph[current]:
            new_cost = g[current] + cost

            if neighbour in CLOSED:
                continue

            if neighbour not in OPEN:
                OPEN.append(neighbour)
                g[neighbour] = new_cost
                parent[neighbour] = current
            else:
                if new_cost < g[neighbour]:
                    g[neighbour] = new_cost
                    parent[neighbour] = current

    return "Failure", None


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

# Call function
path, cost = a_star('A', 'F', graph, heuristic)

print("Path found:", path)
print("Minimum cost:", cost)
