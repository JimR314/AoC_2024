from AoC_Lib import parse_input
from collections import Counter

def part_one(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total = 0
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])
    
    return total

def part_two(left_list, right_list):
    total = 0
    count = Counter(right_list)
    for num in left_list:
        total += num * count[num]
    
    return total

def main():
    lines = parse_input(1, is_live=True)

    left_list = []
    right_list = []

    for line in lines:
        num1, num2 = line.split()
        left_list.append(int(num1))
        right_list.append(int(num2))

    print(part_one(left_list, right_list))
    print(part_two(left_list, right_list))

if __name__ == "__main__":
    main()