import argparse
from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
    
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]
    return rules, updates

def build_graph(rules):
    graph = defaultdict(set)
    for before, after in rules:
        graph[before].add(after)
    return graph

def is_valid_order(update, graph):
    seen = set()
    for page in update:
        if any(dep in seen for dep in graph[page]):
            return False
        seen.add(page)
    return True

def correct_order(update, graph):
    # Sort pages based on their dependencies
    return sorted(update, key=lambda x: sum(1 for dep in graph[x] if dep in update))

def solve(rules, updates):
    graph = build_graph(rules)
    
    valid_updates = [u for u in updates if is_valid_order(u, graph)]
    invalid_updates = [u for u in updates if not is_valid_order(u, graph)]

    part1 = sum(u[len(u) // 2] for u in valid_updates)
    part2 = sum(correct_order(u, graph)[len(u) // 2] for u in invalid_updates)

    return part1, part2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 5 Solution")
    parser.add_argument("input_file", help="Path to the input file")
    args = parser.parse_args()

    rules, updates = parse_input(args.input_file)
    part1, part2 = solve(rules, updates)
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
