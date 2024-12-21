from typing import List


grid: List[List[str]] = []

with open('input.txt', 'r') as f:
    for line in f:
        grid.append([c for c in line])


def grid_contains(r: int, c: int):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def step(r: int, c: int) -> tuple[int, int]:
    d = grid[r][c]

    if d == '^':
        next_pos = (r-1, c) 
    elif d == 'v':
        next_pos = (r+1, c) 
    elif d == '>':
        next_pos = (r, c+1) 
    elif d == '<':
        next_pos = (r, c-1)

    if grid_contains(*next_pos):
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


guard_pos = -1, -1

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] in ['^', '>', 'v', '<']:
            guard_pos = i, j
            

while grid_contains(*guard_pos):
    guard_pos = step(*guard_pos)


ans = 0
for row in grid:
    for c in row:
        if c == 'X':
            ans += 1


print(f'Answer: {ans}')
    



