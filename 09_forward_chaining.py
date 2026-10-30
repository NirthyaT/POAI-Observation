# Experiment 9: Forward Chaining

facts = {"human(socrates)"}

# Each rule is: (list of conditions, conclusion)
rules = [
    (["human(socrates)"], "mortal(socrates)"),
    (["mortal(socrates)"], "wise(socrates)")
]

goal = "wise(socrates)"
iteration = 1

while True:
    new_facts = set()

    # Check whether all conditions of each rule are known.
    for conditions, conclusion in rules:
        if all(condition in facts for condition in conditions):
            if conclusion not in facts:
                new_facts.add(conclusion)

    # Stop if no new facts can be inferred.
    if not new_facts:
        break

    facts.update(new_facts)
    print("Iteration", iteration, "inferred:", new_facts)
    iteration += 1

print("All facts:", facts)
print("Goal derived:", goal in facts)
