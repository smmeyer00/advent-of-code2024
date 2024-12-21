from typing import Dict, List


rules: Dict[int, List[int]]  = {}
updates = []


with open('input.txt', 'r') as f:
    for line in f:
        if not line.strip():
            pass
        elif '|' in line:
            k, v = line.split('|')
            k, v = int(k), int(v)
            if k in rules.keys():
                rules[k].append(v)
            else:
                rules[k] = [v]
        else:
            updates.append([int(x) for x in line.split(',')])


def is_valid(u: List[int]) -> bool:
    seen = set()
    for n in u:
        if n in rules.keys():
            for e in rules[n]:
                if e in seen:
                    return False
        seen.add(n)
                
    return True

def fix_update(u: List[int]):
    while not is_valid(u):
        for l, values in rules.items():
            for r in values:
                if l in u and r in u:
                    l_index = u.index(l)
                    r_index = u.index(r)

                    if l_index > r_index:
                        u[l_index], u[r_index] = u[r_index], u[l_index]

invalid_updates: List[List[int]] = []
for update in updates:
    if not is_valid(update):
        invalid_updates.append(update)

for u in invalid_updates:
    fix_update(u)


ans = 0
for v in invalid_updates:
    ans += v[(len(v)-1) // 2]

print(f'Answer: {ans}')