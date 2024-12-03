from AoC_Lib import parse_input

def part_one(lines):
    total = 0

    for line in lines:
        parts = line.split("mul")
        for part in parts[1:]:

            if part[0] != '(':
                continue
            num1 = ''
            num2 = ''
            valid = True
            section = 0
            for i, char in enumerate(part[1:]):
                if valid == False:
                    break

                if section == 0 and not char.isnumeric():
                    if char == ',':
                        section = 1
                    else:
                        valid = False
                        break
                elif section == 0:
                    num1 += char

                elif section == 1 and not char.isnumeric():
                    valid = False
                    break
                elif section == 1:
                    section = 2
                    num2 += char

                elif section == 2 and not char.isnumeric():
                    if char == ')':
                        break
                    else:
                        valid = False
                        break
                elif section == 2:
                    num2 += char
            
            if valid:
                total += int(num1) * int(num2)
    return total

def curr_state(str, state):
    n = len(str)
    if n < 4:
        return state
    elif n < 7:
        return True if str[-4:] == "do()" else state
    else:
        if str[-7:] == "don't()":
            return False
        elif str[-4:] == "do()":
            return True
        else:
            return state

def part_two(lines):
    total = 0
    do = True

    for line in lines:
        parts = line.split("mul")
        for num, part in enumerate(parts):
            num1 = ''
            num2 = ''
            valid = True
            done = False
            section = 0
            p = part[0]
            do_before = do

            if part[0] != '(':
                valid = False

            for i, char in enumerate(part[1:]):
                p += char
                do = curr_state(p, do)
                
                if do_before and done == False and valid == True:
                    if section == 0 and not char.isnumeric():
                        if char == ',':
                            section = 1
                        else:
                            valid = False
                    elif section == 0:
                        num1 += char

                    elif section == 1 and not char.isnumeric():
                        valid = False
                    elif section == 1:
                        section = 2
                        num2 += char

                    elif section == 2 and not char.isnumeric():
                        if char != ')':
                            valid = False
                        elif char == ')':
                            done = True

                    elif section == 2:
                        num2 += char
            
            if valid and do_before:
                total += int(num1) * int(num2)

            
    return total

def main():
    lines = parse_input(3, is_live=1)

    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()