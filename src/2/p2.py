from typing import List

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

def is_report_safe_with_tolerance(r: List[int]):
    if is_report_safe(r):
        return True 
    
    for i in range(len(r)):
        t = [element for index, element in enumerate(r) if index != i]
        if is_report_safe(t):
            return True 
    
    return False

safe_reports_with_tolerance = 0
for r in reports:
    if is_report_safe_with_tolerance(r):
        safe_reports_with_tolerance += 1

print(f'Safe reports: {safe_reports_with_tolerance}')