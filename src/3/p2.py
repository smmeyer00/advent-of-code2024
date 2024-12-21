from typing import List

memory = ""

with open("input.txt", "r") as f:
    for line in f:
        memory += "x"
        memory += line 


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


def parse_and_sum(line: str) -> int:
    ans = 0
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

    return ans

enabled_subsections = []

start = 0
i = memory.find("don't()", start)
while start >= 0 and i >= 0:
    enabled_subsections.append((start, i))

    start = memory.find("do()", i + 1)
    i = memory.find("don't()", start)

    if start >= 0 and i < 0: # found last do(), will be enabled for rest of mem
        enabled_subsections.append((start, len(memory)))


ans = 0
for l, r in enabled_subsections:
    ans += parse_and_sum(memory[l:r])

print(f'Answer: {ans}')