# Experiment 4: A* Search

import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2), ("D", 5)],
    "B": [("D", 1)],
    "C": [("G", 5)],
    "D": [("G", 3)],
    "G": []
}

# Heuristic estimate h(n) from each node to the goal.
h = {
    "S": 6,
    "A": 5,
    "B": 4,
    "C": 4,
    "D": 2,
    "G": 0
}

# Priority queue entries: (f_score, g_score, node)
open_heap = [(h["S"], 0, "S")]
g_cost = {"S": 0}
parent = {"S": None}
closed = set()

while open_heap:
    f, cost, node = heapq.heappop(open_heap)

    # Ignore an outdated queue entry.
    if cost != g_cost.get(node):
        continue
    if node in closed:
        continue

    print("Expanding:", node, "| OPEN priority:", f)

    if node == "G":
        break

    closed.add(node)

    for neighbour, edge_cost in graph[node]:
        new_cost = cost + edge_cost

        if new_cost < g_cost.get(neighbour, float("inf")):
            g_cost[neighbour] = new_cost
            parent[neighbour] = node
            closed.discard(neighbour)
            new_f = new_cost + h[neighbour]
            heapq.heappush(open_heap, (new_f, new_cost, neighbour))

if "G" in g_cost:
    path = []
    node = "G"

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print("Closed list:", sorted(closed))
    print("Shortest path:", path)
    print("Path cost:", g_cost["G"])
else:
    print("Goal not reachable")
