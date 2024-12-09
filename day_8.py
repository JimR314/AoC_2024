from AoC_Lib import parse_input
from collections import defaultdict

def part_one(nodes, chars, map_width, map_height):
    antinodes = set()

    for char in chars:
        for n1 in nodes[char]:
            for n2 in nodes[char]:
                if n1 == n2:
                    continue
                
                vector = (n2[0] - n1[0], n2[1] - n1[1])
                l1 = (n1[0] - vector[0], n1[1] - vector[1])
                l2 = (n2[0] + vector[0], n2[1] + vector[1])

                if not (l1[0] < 0 or l1[0] >= map_width or l1[1] < 0 or l1[1] >= map_height):
                    antinodes.add(l1)
                if not (l2[0] < 0 or l2[0] >= map_width or l2[1] < 0 or l2[1] >= map_height):
                    antinodes.add(l2)
    
    return len(antinodes)

def part_two(nodes, chars, map_width, map_height):
    antinodes = set()

    for char in chars:
        for n1 in nodes[char]:
            for n2 in nodes[char]:
                if n1 == n2:
                    continue

                antinodes.add(n1)
                antinodes.add(n2)
                
                vector = (n2[0] - n1[0], n2[1] - n1[1])
                l1 = (n1[0] - vector[0], n1[1] - vector[1])
                l2 = (n2[0] + vector[0], n2[1] + vector[1])

                while not (l1[0] < 0 or l1[0] >= map_width or l1[1] < 0 or l1[1] >= map_height):
                    antinodes.add(l1)
                    l1 = (l1[0] - vector[0], l1[1] - vector[1])
                
                while not (l2[0] < 0 or l2[0] >= map_width or l2[1] < 0 or l2[1] >= map_height):
                    antinodes.add(l2)
                    l2 = (l2[0] + vector[0], l2[1] + vector[1])
    
    return len(antinodes)

def main():
    lines = parse_input(8, is_live=1)


    map_width = len(lines[0])
    map_height = len(lines)
    nodes = defaultdict(list)
    chars = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isalnum():
                nodes[char].append((x, y))
                chars.add(char)


    print(part_one(nodes, chars, map_width, map_height))
    print(part_two(nodes, chars, map_width, map_height))

if __name__ == "__main__":
    main()