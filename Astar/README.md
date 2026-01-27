Pseudocode of A* Algorithm


A*(start, goal)

OPEN ← {start}
CLOSED ← ∅

g(start) ← 0
f(start) ← g(start) + h(start)
parent(start) ← NIL

WHILE OPEN is not empty DO

    n ← node in OPEN with minimum f(n)

    IF n = goal THEN
        RETURN path from start to goal using parent pointers

    REMOVE n from OPEN
    ADD n to CLOSED

    FOR each neighbor of n DO

        new_cost ← g(n) + cost(n, neighbor)

        IF neighbor ∈ CLOSED AND new_cost ≥ g(neighbor) THEN
            CONTINUE

        IF neighbor ∉ OPEN OR new_cost < g(neighbor) THEN
            parent(neighbor) ← n
            g(neighbor) ← new_cost
            f(neighbor) ← g(neighbor) + h(neighbor)

            IF neighbor ∉ OPEN THEN
                ADD neighbor to OPEN

END WHILE

RETURN failure




#Code explaination:

def a_star(start, goal, graph, heuristic):
    # OPEN list stores nodes to be explored
    OPEN = [start]

    # CLOSED list stores nodes already explored
    CLOSED = []

    # g dictionary stores cost from start to each node
    g = {}

    # parent dictionary is used to reconstruct the path
    parent = {}

    # Initial cost of start node is zero
    g[start] = 0

    # Start node has no parent
    parent[start] = None

    # Loop until OPEN list is empty
    while OPEN:

        # Select node with minimum f = g + heuristic
        current = OPEN[0]
        for node in OPEN:
            if g[node] + heuristic[node] < g[current] + heuristic[current]:
                current = node

        # If goal is reached, build the path
        if current == goal:
            path = []

            # Trace back from goal to start using parent
            while current is not None:
                path.append(current)
                current = parent[current]

            # Reverse path to get start to goal order
            path.reverse()

            # Minimum cost to reach the goal
            min_cost = g[goal]

            return path, min_cost

        # Move current node from OPEN to CLOSED
        OPEN.remove(current)
        CLOSED.append(current)

        # Explore all neighbouring nodes
        for neighbour, cost in graph[current]:

            # Calculate new cost to reach neighbour
            new_cost = g[current] + cost

            # Ignore neighbour if it is already explored
            if neighbour in CLOSED:
                continue

            # If neighbour is not in OPEN, add it
            if neighbour not in OPEN:
                OPEN.append(neighbour)
                g[neighbour] = new_cost
                parent[neighbour] = current

            # If a cheaper path is found, update cost and parent
            else:
                if new_cost < g[neighbour]:
                    g[neighbour] = new_cost
                    parent[neighbour] = current

    # If goal is not reachable
    return "Failure", None


# Graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values for each node
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

# Call the A* function
path, cost = a_star('A', 'F', graph, heuristic)

# Display result
print("Path found:", path)
print("Minimum cost:", cost)
