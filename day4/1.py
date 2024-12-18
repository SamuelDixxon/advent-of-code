import argparse

'''
Didn't get this one, but had idea from perplexity 
Idea is to scan through grid and do a clocwise 
search around the whole array..
'''

def load_grid_from_file(filename):
    """Load grid from a file."""
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid

def count_xmas(grid):
    """Count occurrences of 'XMAS' in all directions in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0

    # Helper function to check if a word exists in a specific direction
    def check_direction(r, c, dr, dc):
        for i in range(target_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != target[i]:
                return False
        return True

    # Directions: (dr, dc) -> (row change, column change)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal up-left
        (-1, 1)   # Diagonal up-right
    ]

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count

def main():
    parser = argparse.ArgumentParser(description="Count occurrences of 'XMAS' in a word search grid.")
    parser.add_argument('-f', '--file', type=str, help="Optional file name containing the grid")
    args = parser.parse_args()

    if args.file:
        try:
            grid = load_grid_from_file(args.file)
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return
    else:
        # Default hardcoded grid if no file is provided
        grid = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]

    result = count_xmas(grid)
    print(f"Total occurrences of 'XMAS': {result}")

if __name__ == "__main__":
    main()
