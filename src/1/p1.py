left, right = [], []

with open("input.txt", "r") as f:
    for line in f:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

left.sort()
right.sort()

total = 0
for l, r in zip(left, right):
    total += abs(l - r)

print(f'Total diff is: {total}')