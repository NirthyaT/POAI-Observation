# Experiment 5: Minimum and Maximum of Two Numbers

def find_min_max(a, b):
    if a < b:
        minimum = a
        maximum = b
    else:
        minimum = b
        maximum = a

    print("Minimum:", minimum)
    print("Maximum:", maximum)


# Three test cases
find_min_max(10, 20)
find_min_max(7, 3)
find_min_max(5, 5)
