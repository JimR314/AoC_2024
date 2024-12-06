from AoC_Lib import parse_input
from collections import defaultdict

def right_order(rules, update):
    seen = set()

    for page in update:
        seen.add(page)
        for p in rules[page]:
            if p in seen:
                return False
    
    return True

def put_in_order(rules, update):
    seen = set()
    pages = set(update)
    new_update = []

    for _ in range(len(update)):
        remaining = pages - seen
        for page in remaining:
            rule_break = False
            for p in rules[page]:
                if p in pages and p not in seen:
                    rule_break = True
                    break
            if not rule_break:
                new_update.append(page)
                seen.add(page)
    
    return new_update
    
def part_one(rules, updates):
    sum = 0
    for update in updates:
        if right_order(rules, update):
            middle_value = update[(len(update) - 1) // 2]
            sum += middle_value
    return sum

def part_two(rules, updates):
    sum = 0
    for update in updates:
        if not right_order(rules, update):
            new_update = put_in_order(rules, update)

            middle_value = new_update[(len(new_update) - 1) // 2]
            sum += middle_value
    return sum

def main():
    lines = parse_input(5, is_live=0)

    rules = defaultdict(list)
    updates = []
    for line in lines:
        # Rules
        if "|" in line:
            first, second = line.split("|")
            first = int(first)
            second = int(second)

            if first not in rules:
                rules[first] = [second]
            else:
                rules[first].append(second)

        # Updates
        elif "," in line:
            update = [int(i) for i in line.split(",")]
            updates.append(update)


    print(part_one(rules, updates))
    print(part_two(rules, updates))

if __name__ == "__main__":
    main()