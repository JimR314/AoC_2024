from AoC_Lib import parse_input
import time

def get_new_pos(robot, WIDTH, HEIGHT):
    ((sx, sy), (vx, vy)) = robot

    new_x = (sx + vx) % WIDTH
    new_y = (sy + vy) % HEIGHT

    return (new_x, new_y)

def get_quadrant(x, y, width, height):
    mid_x = (width - 1) / 2
    mid_y = (height - 1) / 2
    if x < mid_x:
        if y < mid_y:
            return 0
        elif y > mid_y:
            return 2
    elif x > mid_x:
        if y < mid_y:
            return 1
        elif y > mid_y:
            return 3
    
    return -1


def part_one(robots, WIDTH, HEIGHT):
    
    for _ in range(100):
        new_robots = []
        for robot in robots:
             ((sx, sy), vector) = robot
             new_x, new_y = get_new_pos(robot, WIDTH, HEIGHT)
             new_robots.append(((new_x, new_y), vector))

        robots = new_robots
    
    quadrants = [0, 0, 0, 0]
    for ((sx, sy), (vx, vy)) in robots:
        q = get_quadrant(sx, sy, WIDTH, HEIGHT)
        if q != -1:
            quadrants[q] += 1
    

    product = 1
    for q in quadrants:
        product *= q
    
    return product

def draw_grid(robots, width, height):
    taken = set()
    for ((x, y), vector) in robots:
        taken.add((x, y))
    
    should_print = 0
    to_print = []
    for y in range(height):
        s = ''
        max_run = 0
        run = 0
        for x in range(width):
            if (x, y) in taken:
                run += 1
                s += '#'
            else:
                max_run = max(max_run, run)
                run = 0
                s += '.'
        to_print.append(s)
        if max_run > 8:
            should_print += 1
    
    if should_print >= 2:
        for s in to_print:
            print(s)
        time.sleep(0.5)
        return True


def part_two(robots, WIDTH, HEIGHT):
    seconds = 0
    while seconds < 19000:
        seconds += 1
        new_robots = []
        for robot in robots:
             ((sx, sy), vector) = robot
             new_x, new_y = get_new_pos(robot, WIDTH, HEIGHT)
             new_robots.append(((new_x, new_y), vector))

        if seconds % 500 == 0:
            print(seconds)
        d = draw_grid(new_robots, WIDTH, HEIGHT)
        if d:
            print(f"Seconds passed: {seconds}")
        robots = new_robots

def main():
    live = 1
    if live:
        WIDTH = 101
        HEIGHT = 103
    else:
        WIDTH = 11
        HEIGHT = 7

    lines = parse_input(14, live)

    robots = []
    for line in lines:
        p1, p2 = line.split(' v=')
        sx, sy = p1.split('=')[1].strip().split(',')
        vx, vy = p2.split(',')
        robots.append(((int(sx), int(sy)), (int(vx), int(vy))))
    

    print(part_one(robots, WIDTH, HEIGHT))
    print(part_two(robots, WIDTH, HEIGHT))

if __name__ == "__main__":
    main()