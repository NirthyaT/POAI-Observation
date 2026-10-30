# Experiment 7: Unification and Resolution

def unify(args1, args2):
    """A small teaching example of unification for simple terms."""
    if len(args1) != len(args2):
        return None

    substitution = {}

    for a, b in zip(args1, args2):
        if a == b:
            continue

        if a[0].isupper():          # Uppercase first letter means variable
            substitution[a] = b
        elif b[0].isupper():
            substitution[b] = a
        else:
            return None             # Conflicting constants

    return substitution


print("Unification:", unify(["X", "john"], ["mary", "john"]))

# Propositional resolution:
# Clause 1 = P OR Q
# Clause 2 = NOT P OR R
clause1 = {"P", "Q"}
clause2 = {"NOT P", "R"}

# Remove the complementary literals P and NOT P.
resolvent = (clause1 - {"P"}) | (clause2 - {"NOT P"})

print("Clause 1:", clause1)
print("Clause 2:", clause2)
print("Resolvent:", resolvent)
