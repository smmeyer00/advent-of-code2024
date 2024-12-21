
from typing import List


lines: List[str] = []

with open("input.txt", "r") as f:
    for line in f:
        lines.append(line)


def are_params_valid(s: str):
    if (not s) or (not "," in s):
        return False, 0, 0
    
    t = s.split(",")
    l, r = t[0], t[1]

    if not (l.isdigit() and r.isdigit()):
        return False, 0, 0
    
    l, r = int(l), int(r)

    if not (0 < l < 1000 and 0 < r < 1000):
        return False, 0, 0
    
    return True, l, r



ans = 0
for line_num, line in enumerate(lines):

    # parse line
    start_index = 0
    i = line.find("mul(", start_index)
    while start_index < len(line) and i >= 0:
        end_index = line.find(")", i)
        if end_index:
            valid, n1, n2 = are_params_valid(line[i+4:end_index])
            if valid:
                ans += (n1 * n2)

        start_index = i + 1
        i = line.find("mul(", start_index)


print(f'Answer: {ans}')