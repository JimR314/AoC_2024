from AoC_Lib import parse_input

def get_neighbour_coords(grid, x, y):
    search_val = str(int(grid[y][x]) + 1)
    coords = []

    for j in [-1, 1]:
        if grid[y+j][x] == search_val:
            coords.append((x, y+j))
    for i in [-1, 1]:
        if grid[y][x+i] == search_val:
            coords.append((x+i, y))
    
    return coords

def part_one(lines):
    sum = 0
    zeros = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "0":
                zeros.append((x, y))
    
    for (x, y) in zeros:
        nines = set()
        search_list = [(x, y)]
        for _ in range(9):
            new_search_list = []
            for (x, y) in search_list:
                new_search_list.extend(get_neighbour_coords(lines, x, y))
            search_list = new_search_list
        nines.update(search_list)
        score = len(nines)
        sum += score
    
    return sum

def part_two(lines):
    total = 0
    zeros = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "0":
                zeros.append((x, y))
    
    def get_rating(grid, x, y, search_list):
        if grid[y][x] == "9":
            return 1
        elif search_list == []:
            return 0
        return sum([get_rating(grid, int(x), int(y), get_neighbour_coords(grid, int(x), int(y))) for (x, y) in search_list])

    for (x, y) in zeros:
        total += get_rating(lines, x, y, get_neighbour_coords(lines, x, y))
    
    return total

def main():
    lines = parse_input(10, is_live=0)

    # Add buffer
    for i in range(len(lines)):
        lines[i] = "." + lines[i] + "."
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))

    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()