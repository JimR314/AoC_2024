from AoC_Lib import parse_input

def count_ways_to_form_design(design, patterns):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if dp[i] == 0:
            continue
        for pat in patterns:
            plen = len(pat)
            if i + plen <= n and design[i:i+plen] == pat:
                dp[i + plen] += dp[i]

    return dp[n]

def part_one(lines):
    patterns_line = lines[0].strip()
    patterns = [p.strip() for p in patterns_line.split(',')]
    
    blank_index = None
    for idx, line in enumerate(lines[1:], 1):
        if line.strip() == "":
            blank_index = idx
            break
    
    designs = lines[blank_index+1:]
    
    count = 0
    for design in designs:
        design = design.strip()
        if count_ways_to_form_design(design, patterns) > 0:
            count += 1
    return count

def part_two(lines):
    patterns_line = lines[0].strip()
    patterns = [p.strip() for p in patterns_line.split(',')]
    
    blank_index = None
    for idx, line in enumerate(lines[1:], 1):
        if line.strip() == "":
            blank_index = idx
            break
    
    designs = lines[blank_index+1:]

    total_ways = 0
    for design in designs:
        design = design.strip()
        ways = count_ways_to_form_design(design, patterns)
        total_ways += ways
    return total_ways

def main():
    lines = parse_input(19, is_live=1)
    
    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()
