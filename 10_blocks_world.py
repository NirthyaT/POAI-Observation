# Experiment 10: Blocks World

# Each key is a block. Its value tells what it is on.
on = {
    "A": "table",
    "B": "table",
    "C": "table"
}

hand = None


def pickup(block):
    global hand

    # Pick up a block only if the hand is empty
    # and the block is on the table.
    if hand is None and on[block] == "table":
        hand = block
        on[block] = "hand"
        print("PICKUP", block)
    else:
        print("Cannot PICKUP", block)


def stack(block, target):
    global hand

    # Stack the held block on the target block.
    if hand == block and on[target] != "hand":
        on[block] = target
        hand = None
        print("STACK", block, "on", target)
    else:
        print("Cannot STACK", block, "on", target)


print("Initial state:", on)

pickup("B")
stack("B", "C")

pickup("A")
stack("A", "B")

print("Goal state:", on)
print("Goal reached:", on["A"] == "B" and on["B"] == "C")
