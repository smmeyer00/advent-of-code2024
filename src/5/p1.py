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

valid_updates: List[List[int]] = []
for update in updates:
    if is_valid(update):
        valid_updates.append(update)


ans = 0
for v in valid_updates:
    ans += v[(len(v)-1) // 2]

print(f'Answer: {ans}')
        
    