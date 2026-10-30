# Experiment 3: MINIMAX Algorithm

# A is the MAX root. B and C are MIN nodes.
# D, E, F and G are terminal nodes with the given scores.
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

scores = {
    "D": 3,
    "E": 5,
    "F": 1,
    "G": -1
}


def minimax(node, is_max):
    # A node with no children is a leaf.
    if len(tree[node]) == 0:
        print("Leaf", node, "value =", scores[node])
        return scores[node]

    values = []
    for child in tree[node]:
        values.append(minimax(child, not is_max))

    if is_max:
        value = max(values)
    else:
        value = min(values)

    print("Node", node, "value =", value)
    return value


best_value = minimax("A", True)

# Evaluate each root move to identify the optimal move.
root_values = {}
for child in tree["A"]:
    root_values[child] = minimax(child, False)

optimal_move = max(root_values, key=root_values.get)

print("Best value for MAX:", best_value)
print("Optimal move:", optimal_move)
