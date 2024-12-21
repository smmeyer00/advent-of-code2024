left_list, r_freq_map = [], {}

with open("input.txt", "r") as f:
    for line in f:
        nums = line.split()
        left_list.append(int(nums[0]))
        
        r_num = int(nums[1])
        if r_num in r_freq_map.keys():
            r_freq_map[r_num] = r_freq_map[r_num] + 1
        else:
            r_freq_map[r_num] = 1

sim_score = 0
for e in left_list:
    if e in r_freq_map.keys():
        sim_score += (e * r_freq_map[e])

print(f'Sim score: {sim_score}')
        


