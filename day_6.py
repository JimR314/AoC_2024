from AoC_Lib import parse_input

def turn_right(direction):
    return [-direction[1], direction[0]]

def get_new_pos(pos, direction):
    return [pos[0] + direction[0], pos[1] + direction[1]]

def part_one(start_pos, obstacles, map_length, map_height):
    visited = set()
    total_visited = 1

    current_pos = start_pos
    current_direction = [0, -1]

    visited.add(tuple(current_pos))
    while True:
        if tuple(get_new_pos(current_pos, current_direction)) in obstacles:
            current_direction = turn_right(current_direction)
            continue
        else:
            current_pos = get_new_pos(current_pos, current_direction)
            if tuple(current_pos) not in visited:
                visited.add(tuple(current_pos))
                total_visited += 1
            
        if current_pos[0] < 0 or current_pos[0] >= map_length or current_pos[1] < 0 or current_pos[1] >= map_height:
            total_visited -= 1
            break


    return total_visited

def part_two(start_pos, obstacles, map_length, map_height):
    num_spots = 0

    for y in range(map_height):
        for x in range(map_length):
            if (x, y) in obstacles:
                continue
            if (x, y) == tuple(start_pos):
                continue
            
            obstacles.add((x, y))
            states = set()

            current_pos = start_pos
            current_direction = [0, -1]

            while True:

                if tuple(get_new_pos(current_pos, current_direction)) in obstacles:
                    current_direction = turn_right(current_direction)
                    continue
                else:
                    current_pos = get_new_pos(current_pos, current_direction)
                    if tuple([current_pos[0], current_pos[1], current_direction[0], current_direction[1]]) in states:
                        num_spots += 1
                        break
                    states.add(tuple([current_pos[0], current_pos[1], current_direction[0], current_direction[1]]))


                if current_pos[0] < 0 or current_pos[0] >= map_length or current_pos[1] < 0 or current_pos[1] >= map_height:
                    break
            
            obstacles.remove((x, y))


    return num_spots

def main():
    lines = parse_input(6, is_live=1)

    obstacles = set()
    start_pos = None
    map_length = len(lines[0])
    map_height = len(lines)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char == '^':
                start_pos = [x, y]
    
    if start_pos is None:
        raise ValueError("No start position found")

    print(part_one(start_pos, obstacles, map_length, map_height))
    print(part_two(start_pos, obstacles, map_length, map_height))

if __name__ == "__main__":
    main()