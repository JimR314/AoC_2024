from AoC_Lib import parse_input
from itertools import product

def part_one(equations):
    total = 0

    for eq in equations:
        found = False
        if found:
            break
        num_ops = len(eq[1]) - 1
        for i in range(2 ** num_ops):
            t = 0
            bin_str = str(bin(i))[2:]
            if len(bin_str) < num_ops:
                bin_str = "0" * (num_ops - len(bin_str)) + bin_str
            ops = "+"
            for char in bin_str:
                if char == "0":
                    ops += "+"
                else:
                    ops += "*"
            
            for i, num in enumerate(eq[1]):
                if ops[i] == "+":
                    t += num
                else:
                    t *= num
            if t == eq[0]:
                total += t
                found = True
                break
    
    return total
            

def part_two(equations):
    total = 0
    operations = ["+", "*", '||']

    for eq in equations:
        print(eq[0])
        found = False
        if found:
            break
        num_ops = len(eq[1]) - 1
        all_ops = [['+'] + list(p) for p in product(operations, repeat=num_ops)]
        for ops in all_ops:
            t = 0
            for i, num in enumerate(eq[1]):
                if ops[i] == "+":
                    t += num
                elif ops[i] == "*":
                    t *= num
                else:
                    t = int(str(t) + str(num))
            if t == eq[0]:
                total += t
                found = True
                break
    
    return total

def main():
    lines = parse_input(7, is_live=1)

    equations = []
    for line in lines:
        total, nums = line.split(": ")
        total = int(total)
        nums = list(map(int, nums.split(" ")))
        equations.append((total, nums))

    print(part_one(equations))
    print(part_two(equations))

if __name__ == "__main__":
    main()