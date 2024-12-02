from AoC_Lib import parse_input

def is_safe(report):
    increasing = True if report[1] > report[0] else False
    for i, num in enumerate(report[:-1]):
        diff = report[i+1] - num
        if increasing and not (1 <= diff <= 3):
            return False
        elif not increasing and not (-3 <= diff <= -1):
            return False
    return True

def part_one(nums):
    total = 0

    for report in nums:
        safe = is_safe(report)
        if safe:
            total += 1
    
    return total

def part_two(nums):
    total = 0

    for report in nums:
        safe = is_safe(report)
        if not safe:
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                safe = is_safe(new_report)
                if safe:
                    total += 1
                    break
        else:
            total += 1
    
    return total


def main():
    lines = parse_input(2, is_live=True)

    reports = []

    for line in lines:
        report = [int(n) for n in line.split()]
        reports.append(report)

    print(part_one(reports))
    print(part_two(reports))

if __name__ == "__main__":
    main()