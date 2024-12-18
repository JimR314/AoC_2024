from AoC_Lib import parse_input

def get_vector(instruction):
    if instruction == '^':
        return (0, -1)
    elif instruction == 'v':
        return (0, 1)
    elif instruction == '<':
        return (-1, 0)
    elif instruction == '>':
        return (1, 0)

def move_robot(boxes, robot, instruction, walls):
    x, y = robot
    vector = get_vector(instruction)

    to_move = []
    check_x, check_y = x, y
    while True:
        check_pos = check_x + vector[0], check_y + vector[1]
        if check_pos in boxes:
            to_move.append(check_pos)
            check_x, check_y = check_pos
        elif check_pos in walls:
            return boxes, robot
        else:
            break
    
    for box in to_move[::-1]:
        boxes.remove(box)
        boxes.add((box[0] + vector[0], box[1] + vector[1]))
    robot = (x + vector[0], y + vector[1])
    
    return boxes, robot

def part_one(warehouse, instructions):
    walls = set()
    boxes = set()
    for y, line in enumerate(warehouse):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            elif char == 'O':
                boxes.add((x, y))
            elif char == '@':
                robot = (x, y)
    
    for instruction in instructions:
        boxes, robot = move_robot(boxes, robot, instruction, walls)
    
    # for y, line in enumerate(warehouse):
    #     s = ''
    #     for x, char in enumerate(line):
    #         if (x, y) in boxes:
    #             s += 'O'
    #         elif (x, y) == robot:
    #             s += '@'
    #         else:
    #             if char == '#':
    #                 s += char
    #             else:
    #                 s += '.'
    #     print(s)

    total = 0
    for box in boxes:
        total += 100 * box[1] + box[0]
    
    return total

def stretch_move(boxes, robot, instruction, walls):
    x, y = robot
    vector = get_vector(instruction)

    to_move = []
    checked = set()
    to_check = [(x, y)]
    while True:
        check_next = []
        for (check_x, check_y) in to_check:
            checked.add((check_x, check_y))
            check_pos = check_x + vector[0], check_y + vector[1]
            box_left = (check_pos[0] - 1, check_pos[1])
            if check_pos in walls:
                return boxes, robot
            elif check_pos in boxes:
                if check_pos not in to_move:
                    to_move.append(check_pos)
                if check_pos not in checked:
                    check_next.append(check_pos)
                if (check_pos[0] + 1, check_pos[1]) not in checked:
                    check_next.append((check_pos[0] + 1, check_pos[1]))
            elif box_left in boxes:
                if box_left not in to_move:
                    to_move.append(box_left)
                if box_left not in checked:
                    check_next.append(box_left)
                if check_pos not in checked:
                    check_next.append(check_pos)
        
        if len(check_next) == 0:
            break
        to_check = check_next
    
    for box in to_move[::-1]:
        boxes.remove(box)
        boxes.add((box[0] + vector[0], box[1] + vector[1]))
    robot = (x + vector[0], y + vector[1])
    
    return boxes, robot

def draw_warehouse(warehouse, boxes, robot, walls):
    print(boxes, robot)
    for y, line in enumerate(warehouse):
        s = ''
        for x, char in enumerate(line):
            if (x, y) in boxes:
                s += '[]'
            elif (x-1, y) in boxes:
                continue
            elif (x, y) == robot:
                s += '@'
            elif (x, y) in walls:
                s += '#'
            else:
                s += '.'
        print(s)
    print('\n')

def calc_total(height, width, boxes):
    total = 0
    for box in boxes:
        total += 100 * box[1] + box[0]
    
    return total

def part_two(warehouse, instructions):
    walls = set()
    boxes = set()
    new_warehouse = []
    for y, line in enumerate(warehouse):
        new_line = ''
        for x, char in enumerate(line):
            if char == '#':
                new_line += '##'
                walls.add((2*x, y))
                walls.add((2*x+1, y))
            elif char == 'O':
                new_line += '[]'
                boxes.add((2*x, y))
            elif char == '@':
                new_line += '@.'
                robot = (2*x, y)
            else:
                new_line += '..'
        new_warehouse.append(new_line)
    
    for instruction in instructions:
        boxes, robot = stretch_move(boxes, robot, instruction, walls)
    
    
    height = len(new_warehouse)
    width = max([len(line) for line in new_warehouse])

    return calc_total(height, width, boxes)

def main():
    lines = parse_input(15, is_live=1)

    warehouse = []
    instructions = []

    for line in lines:
        if line == "":
            continue
        if line[0] == '#':
            warehouse.append(line)
        else:
            for instruction in line:
                instructions.extend(instruction)

    print(part_one(warehouse, instructions))
    print(part_two(warehouse, instructions))

if __name__ == "__main__":
    main()