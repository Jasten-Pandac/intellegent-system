import random

def generate_sudoku():
    n = 9
    grid = [[0 for _ in range(n)] for _ in range(n)]
    numbers = list(range(1, n + 1))
    
    def is_valid(row, col, num):
        # Check if the number is already in the row or column
        for i in range(n):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        
        # Check if the number is in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku():
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(row, col, num):
                            grid[row][col] = num
                            if solve_sudoku():
                                return True
                            grid[row][col] = 0
                    return False
        return True

    # Start filling the Sudoku grid
    solve_sudoku()
    return grid

def print_sudoku(grid):
    for row in grid:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    sudoku = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_sudoku(sudoku)
