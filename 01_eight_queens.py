# Experiment 1: Eight Queens using Backtracking

N = 8
board = [-1] * N
solutions = 0
first_solution = None


def is_safe(row, col):
    """Check whether a queen can be placed at (row, col)."""
    for previous_row in range(row):
        previous_col = board[previous_row]

        # Same column or same diagonal
        if previous_col == col:
            return False
        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve(row):
    global solutions, first_solution

    # All 8 rows have been filled: one solution is found.
    if row == N:
        solutions += 1
        if first_solution is None:
            first_solution = board.copy()
        return

    # Try every column in the current row.
    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            solve(row + 1)       # Place queen in the next row
            board[row] = -1      # Backtrack


solve(0)

print("One valid board:")
for row in range(N):
    print(" ".join("Q" if first_solution[row] == col else "."
                   for col in range(N)))

print("Total solutions:", solutions)
