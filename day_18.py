from AoC_Lib import parse_input

def part_one(fallen, width, height):
    start = (0, 0)
    end = (width - 1, height - 1)
    
    def get_valid_neighbours(x, y):
        neighbours = []
        if x + 1 < width:
            neighbours.append((x + 1, y))
        if x - 1 >= 0:
            neighbours.append((x - 1, y))
        if y + 1 < height:
            neighbours.append((x, y + 1))
        if y - 1 >= 0:
            neighbours.append((x, y - 1))
        return [n for n in neighbours if n not in fallen]

    def bfs(start, end, fallen):
        queue = [(start, 0)]
        visited = set()
        while queue:
            (x, y), dist = queue.pop(0)
            if (x, y) == end:
                return dist
            if (x, y) in visited:
                continue
            if (x, y) in fallen:
                continue
            visited.add((x, y))
            for neighbour in get_valid_neighbours(x, y):
                if neighbour not in visited:
                    queue.append((neighbour, dist + 1))
    
    return bfs(start, end, fallen)

def part_two(fully_fallen, width, height):
    i = 0
    while True:
        i += 1
        fallen = set(fully_fallen[:i])
        dist = part_one(fallen, width, height)
        if part_one(fallen, width, height) is None:
            return fully_fallen[i-1]

def main():
    is_live = 1
    if is_live:
        width, height = 71, 71
    else:
        width, height = 7, 7

    lines = parse_input(18, is_live)

    fallen = set()
    fully_fallen = []
    for i, line in enumerate(lines):
        x, y = line.split(",")
        if is_live and i <= 1023:
            fallen.add((int(x), int(y)))
        elif not is_live and i <= 11:
            fallen.add((int(x), int(y)))
        fully_fallen.append((int(x), int(y)))

    print(part_one(fallen, width, height))
    print(part_two(fully_fallen, width, height))

if __name__ == '__main__':
    main()