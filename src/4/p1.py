from typing import List


grid = []

with open("input.txt", "r") as f:
    for line in f:
        grid.append(line)

def valid_pos(r: int, c: int) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[1])

dir_offsets = [
    [[-1, 0], [-2, 0], [-3, 0]], # up
    [[1, 0], [2, 0], [3, 0]], # down
    [[0, 1], [0, 2], [0, 3]], # right
    [[0, -1], [0, -2], [0, -3]], # left

    [[-1, -1], [-2, -2], [-3, -3]], # up left
    [[-1, 1], [-2, 2], [-3, 3]], # up right
    [[1, -1], [2, -2], [3, -3]], # down left
    [[1, 1], [2, 2], [3, 3]], # down right
]

def get_positions(start_row: int, start_col: int, offsets: List[List[int]]) -> str:
    s = ""
    for r, c in offsets:
        r += start_row
        c += start_col
        if valid_pos(r, c):
            s += grid[r][c]
    return s

count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'X':
            for dir_offset in dir_offsets:
                if get_positions(r, c, dir_offset) == 'MAS':
                    count += 1

print(f'Occurrences: {count}')