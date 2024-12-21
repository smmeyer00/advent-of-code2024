from typing import List


grid: List[str] = []

with open("input.txt", "r") as f:
    for line in f:
        grid.append(line)


def is_valid_xmas(r: int, c: int) -> bool:
    # check first diagonal
    t = grid[r-1][c-1]+grid[r+1][c+1]
    if not (t == 'MS' or t == 'SM'):
        return False 
    
    t = grid[r-1][c+1]+grid[r+1][c-1]
    if not (t == 'MS' or t == 'SM'):
        return False 
    
    return True


count = 0
for r in range(1, len(grid)-1):
    for c in range(1, len(grid[0])-1):
        if grid[r][c] == 'A' and is_valid_xmas(r, c):
            count += 1


print(f'Occurrences: {count}')


