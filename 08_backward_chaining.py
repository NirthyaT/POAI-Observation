# Experiment 8: Backward Chaining

facts = {"human(socrates)"}

# Each dictionary key is a conclusion.
# Its list contains the conditions that must be proved.
rules = {
    "mortal(socrates)": ["human(socrates)"],
    "wise(socrates)": ["mortal(socrates)"]
}


def prove(goal):
    print("Goal:", goal)

    # A goal already present in facts is proved.
    if goal in facts:
        print("Found as a fact:", goal)
        return True

    # Otherwise, try the rule that can produce this goal.
    if goal in rules:
        for subgoal in rules[goal]:
            print(" To prove", goal, "we need", subgoal)

            if not prove(subgoal):
                return False

        print("Proved:", goal)
        return True

    print("Cannot prove:", goal)
    return False


print("Result:", prove("wise(socrates)"))
