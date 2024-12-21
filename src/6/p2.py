from typing import Dict, List
import copy 


original_grid: List[List[str]] = []

with open('input.txt', 'r') as f:
    for line in f:
        original_grid.append([c for c in line])


def grid_contains(grid: List[List[str]], r: int, c: int):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def step(grid: List[List[str]], r: int, c: int) -> tuple[int, int]:
    d = grid[r][c]

    if d == '^':
        next_pos = (r-1, c) 
    elif d == 'v':
        next_pos = (r+1, c) 
    elif d == '>':
        next_pos = (r, c+1) 
    elif d == '<':
        next_pos = (r, c-1)

    if grid_contains(grid, *next_pos):
        if grid[next_pos[0]][next_pos[1]] == '#':
            if d == '^':
                grid[r][c] = '>'
            elif d == '>':
                grid[r][c] = 'v'
            elif d == 'v':
                grid[r][c] = '<'
            elif d == '<':
                grid[r][c] = '^'

            return (r, c)
        
        grid[next_pos[0]][next_pos[1]] = d 
    
    grid[r][c] = 'X'
    return next_pos

def does_loop_exist(grid: List[List[str]], r: int, c: int) -> bool:
    visited: Dict[tuple[int, int], List[str]] = {}

    visited[(r, c)] = [grid[r][c]]

    while grid_contains(grid, r, c):
        r, c = step(grid, r, c)
        
        if (r,c) in visited.keys():
            if grid[r][c] in visited[(r, c)]:
                return True
            visited[(r, c)].append(grid[r][c])
        else:
            visited[(r, c)] = []

    return False


guard_pos = -1, -1
for i in range(len(original_grid)):
    for j in range(len(original_grid[0])):
        if original_grid[i][j] in ['^', '>', 'v', '<']:
            guard_pos = i, j
            
ans = 0
for i in range(len(original_grid)):
    for j in range(len(original_grid[0])):
        if original_grid[i][j] == '.':
            print(f'Trying to flip {i},{j}')
            copy_grid = copy.deepcopy(original_grid)
            copy_grid[i][j] = '#'
            if does_loop_exist(copy_grid, guard_pos[0], guard_pos[1]):
                ans += 1

print(f'Answer: {ans}')



