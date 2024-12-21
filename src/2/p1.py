reports = []

with open("input.txt", "r") as f:
    for line in f:
        reports.append([int(x) for x in line.split()])

def is_report_safe(r):
    if not (r == sorted(r) or r == sorted(r, reverse=True)):
        return False 
    
    for i in range(len(r)-1):
        if not (1 <= abs(r[i] - r[i+1]) <= 3):
            return False 
        
    return True


safe_reports = 0
for r in reports:
    if is_report_safe(r):
        safe_reports += 1

print(f'Safe reports: {safe_reports}')