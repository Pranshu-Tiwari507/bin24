N = 8
def is_safe(solution, row, col):
    for prev_row in range(1, row):
        prev_col = solution[prev_row]
        if prev_col == col:
            return False
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True
def backtrack(solution, row):
    if row > N:
        return True
    for col in range(1, N + 1):
        if is_safe(solution, row, col):
            solution[row] = col
            if backtrack(solution, row + 1):
                return True
            del solution[row]
    return False
def print_board(solution):
    for row in range(1, N + 1):
        line = ""
        for col in range(1, N + 1):
            line += "Q " if solution[row] == col else ". "
        print(line.strip())
def main():
    solution = {}
    if backtrack(solution, 1):
        result = [solution[r] for r in range(1, N + 1)]
        print("Solution found:", result)
        print()
        for r in range(1, N + 1):
            print(f"Q{r} -> Row {r}, Column {solution[r]}")
        print()
        print_board(solution)
    else:
        print("No solution exists.")
if __name__ == "__main__":
    main()