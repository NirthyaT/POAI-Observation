# Experiment 11: Fuzzy Inference System

def low(x):
    """Membership value in the LOW fuzzy set."""
    return max(0, min(1, (7 - x) / 4))


def high(x):
    """Membership value in the HIGH fuzzy set."""
    return max(0, min(1, (x - 3) / 4))


def calculate_tip(service, food):
    s_low = low(service)
    s_high = high(service)
    f_low = low(food)
    f_high = high(food)

    # Each rule is (rule strength, output tip percentage).
    # min() represents the AND operation.
    rules = [
        (min(s_low, f_low), 5),     # Low service and low food
        (min(s_low, f_high), 10),   # Low service and high food
        (min(s_high, f_low), 10),   # High service and low food
        (min(s_high, f_high), 20)   # High service and high food
    ]

    numerator = sum(strength * value for strength, value in rules)
    denominator = sum(strength for strength, value in rules)

    # Avoid division by zero.
    if denominator == 0:
        return 0

    # Weighted-average defuzzification.
    return numerator / denominator


# Two test inputs
test_inputs = [(2, 8), (8, 9)]

for service, food in test_inputs:
    result = calculate_tip(service, food)
    print("Service =", service,
          "Food =", food,
          "Tip =", round(result, 2), "%")
