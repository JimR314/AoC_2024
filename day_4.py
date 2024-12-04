from AoC_Lib import parse_input

def xmas_count(lines):
    # Search 7x7 area


    count = 0
    if lines[3][3:] == "XMAS":
        count += 1
    if lines[3][:4] == "SAMX":
        count += 1
    

    if [line[3] for line in lines[:3]] == ["S", "A", "M"]:
        count += 1
    if [line[3] for line in lines[4:]] == ["M", "A", "S"]:
        count += 1
    
    # Now diagonals

    if [lines[i][i] for i in range(3)] == ["S", "A", "M"]:
        count += 1
    if [lines[i][7-i-1] for i in range(3)] == ["S", "A", "M"]:
        count += 1
    if [lines[7-i-1][i] for i in range(3)] == ["S", "A", "M"]:
        count += 1
    if [lines[7-i-1][7-i-1] for i in range(3)] == ["S", "A", "M"]:
        count += 1
    
    return count

def part_one(lines):
    total = 0

    num_lines = len(lines)
    line_len = len(lines[0])

    for i in range(num_lines):
        lines[i] = "." + "." + "." + lines[i] + "." + "." + "."
    
    pad_string = "." * (line_len + 6)
    new_lines = [pad_string for _ in range(3)]
    for line in lines:
        new_lines.append(line)
    for _ in range(3):
        new_lines.append(pad_string)
    
    for i, line in enumerate(new_lines):
        for j, char in enumerate(line):
            if char == "X":
                total += xmas_count([new_lines[k][j-3:j+4] for k in range(i-3, i+4)])
    
    return total

def x_mas_count(lines):
    if lines[0][0] == 'M':
        if lines[0][2] == 'M':
            if lines[2][0] == 'S' and lines[2][2] == 'S':
                return True
        elif lines[0][2] == 'S':
            if lines[2][0] == 'M' and lines[2][2] == 'S':
                return True
    elif lines[0][0] == 'S':
        if lines[0][2] == 'M':
            if lines[2][0] == 'S' and lines[2][2] == 'M':
                return True
        elif lines[0][2] == 'S':
            if lines[2][0] == 'M' and lines[2][2] == 'M':
                return True
    
    return False

def part_two(lines):
    total = 0

    num_lines = len(lines)
    line_len = len(lines[0])


    for i in range(num_lines):
        lines[i] = "." + lines[i] + "."
    
    pad_string = "." * (line_len + 2)
    new_lines = [pad_string for _ in range(1)]
    for line in lines:
        new_lines.append(line)
    for _ in range(1):
        new_lines.append(pad_string)
    
    for i, line in enumerate(new_lines):
        for j, char in enumerate(line):
            if char == "A":
                total += x_mas_count([new_lines[k][j-1:j+2] for k in range(i-1, i+2)])
    
    return total

def main():
    lines = parse_input(4, is_live=0)

    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()