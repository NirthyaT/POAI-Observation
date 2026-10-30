# Experiment 2: Depth First Search (DFS)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": ["H"],
    "H": []
}

visited = set()
traversal_order = []
parent = {}


def dfs(node, goal):
    visited.add(node)
    traversal_order.append(node)

    if node == goal:
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            parent[neighbour] = node
            if dfs(neighbour, goal):
                return True

    return False


start = "A"
goal = "H"
parent[start] = None

found = dfs(start, goal)

print("DFS traversal:", traversal_order)

if found:
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print("Path:", path)
else:
    print("Goal not found")
