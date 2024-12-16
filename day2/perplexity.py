def is_safe_report(levels):
    if len(levels) < 2:
        return True
    
    increasing = levels[1] > levels[0]
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        if increasing and diff <= 0:
            return False
        if not increasing and diff >= 0:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return True

def find_minimum_change(levels):
    if is_safe_report(levels):
        return 0
    
    min_changes = float('inf')
    for i in range(len(levels)):
        for change in [-3, -2, -1, 1, 2, 3]:
            new_levels = levels.copy()
            new_levels[i] += change
            if is_safe_report(new_levels):
                return 1
    
    for i in range(len(levels)):
        for change in [-3, -2, -1, 1, 2, 3]:
            new_levels = levels.copy()
            new_levels[i] += change
            sub_changes = find_minimum_change(new_levels)
            if sub_changes < float('inf'):
                min_changes = min(min_changes, 1 + sub_changes)
    
    return min_changes

def process_reports(filename):
    safe_count = 0
    total_changes = 0
    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_safe_report(levels):
                safe_count += 1
            total_changes += find_minimum_change(levels)
    return safe_count, total_changes

# Main execution
input_file = 'input.txt'
safe_reports, minimum_changes = process_reports(input_file)
print(f"Part 1 - Number of safe reports: {safe_reports}")
print(f"Part 2 - Total minimum changes required: {minimum_changes}")
