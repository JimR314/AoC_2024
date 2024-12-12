from AoC_Lib import parse_input

def get_neighbours(grid, x, y):
    char = grid[y][x]
    neighbours = []
    if x > 0:
        if grid[y][x-1] == char:
            neighbours.append((x-1, y))
    if x < len(grid[0]) - 1:
        if grid[y][x+1] == char:
            neighbours.append((x+1, y))
    if y > 0:
        if grid[y-1][x] == char:
            neighbours.append((x, y-1))
    if y < len(grid) - 1:
        if grid[y+1][x] == char:
            neighbours.append((x, y+1))
    
    return neighbours

def search_area(grid, x, y):
    found = set()
    search_list = [(x, y)]
    found.add((x, y))
    while search_list != []:
        cur_x, cur_y = search_list[0]
        neighbours = get_neighbours(grid, cur_x, cur_y)
        for n in neighbours:
            if n in found:
                continue
            found.add(n)
            search_list.append(n)
        
        search_list.pop(0)
    
    return found

def find_regions(grid):
    seen = set()
    regions = []

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if (x, y) in seen:
                continue
            region = search_area(grid, x, y)
            seen.update(region)
            regions.append(region)
    
    return regions

def get_perimeter(grid, region):
    total = 0
    for (x, y) in region:
        total += 4 - len(get_neighbours(grid, x, y))
    
    return total

def get_sides(grid, region):
    sides = set()
    for (x, y) in region:
        sides.add((x, y, x-1, y))
        sides.add((x, y, x+1, y))
        sides.add((x, y, x, y-1))
        sides.add((x, y, x, y+1))
        neighbours = get_neighbours(grid, x, y)
        for (w, z) in neighbours:
            sides.remove((x, y, w, z))
    
    return sides


def get_num_sides(grid, region):
    sides = get_sides(grid, region)
    total = 0

    while len(sides) > 0:
        search_list = [sides.pop()]
        sides.add(search_list[0])
        removed = set()
        while search_list != []:
            x, y, w, z = search_list.pop(0)
            sides.remove((x, y, w, z))
            removed.add((x, y, w, z))

            if x == w:
                if (x-1, y, w-1, z) in sides:
                    search_list.append((x-1, y, w-1, z))
                if (x+1, y, w+1, z) in sides:
                    search_list.append((x+1, y, w+1, z))

            elif y == z:
                if (x, y-1, w, z-1) in sides:
                    search_list.append((x, y-1, w, z-1))
                if (x, y+1, w, z+1) in sides:
                    search_list.append((x, y+1, w, z+1))
        total += 1
    
    return total

def part_one(lines):
    return sum([len(region) * get_perimeter(lines, region) for region in find_regions(lines)])

def part_two(lines):
    return sum([len(region) * get_num_sides(lines, region) for region in find_regions(lines)])

def main():
    lines = parse_input(12, is_live=1)

    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()