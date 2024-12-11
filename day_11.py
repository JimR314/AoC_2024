from AoC_Lib import parse_input
from collections import defaultdict

def get_new_nums(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        return [int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])]
    else:
        return [num * 2024]

def part_one(nums, num_blinks=25):
    num_dict = defaultdict(int)

    for num in nums:
        num_dict[num] += 1
    
    for blink in range(num_blinks):
        new_dict = defaultdict(int)
        size = 0
        for key in num_dict:
            new_nums = get_new_nums(key)
            for num in new_nums:
                new_dict[num] += num_dict[key]
                size += num_dict[key]
        num_dict = new_dict
    
    return size

def part_two(nums):
    return part_one(nums, 75)

def main():
    lines = parse_input(11, is_live=1)

    nums = [int(x) for x in lines[0].split(" ")]

    print(part_one(nums))
    print(part_two(nums))

if __name__ == "__main__":
    main()