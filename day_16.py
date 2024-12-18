from AoC_Lib import parse_input
import heapq
from collections import defaultdict
import time

def rotate_clockwise(direction):
    return (direction[1], -direction[0])

def rotate_anticlockwise(direction):
    return (-direction[1], direction[0])

def bfs(walls, start, end):
    initial_direction = (1, 0)
    queue = []
    heapq.heappush(queue, (0, start, initial_direction))
    visited = set()
    while queue:
        cost, pos, direction = heapq.heappop(queue)
        if pos == end:
            return cost
        
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))
        
        x, y = pos
        if (x + direction[0], y + direction[1]) not in walls:
            heapq.heappush(queue, (cost + 1, (x + direction[0], y + direction[1]), direction))
        turn_right = rotate_clockwise(direction)
        turn_left = rotate_anticlockwise(direction)
        heapq.heappush(queue, (cost + 1000, pos, turn_right))
        heapq.heappush(queue, (cost + 1000, pos, turn_left))

def part_one(walls, start, end):
    return bfs(walls, start, end)

def bfs_modified(walls, start, end):
    initial_direction = (1, 0)
    queue = []
    heapq.heappush(queue, (0, start, initial_direction))
    visited = set()
    while queue:
        cost, pos, direction = heapq.heappop(queue)
        if pos == end:
            return cost
        
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))
        
        x, y = pos
        if (x + direction[0], y + direction[1]) not in walls:
            heapq.heappush(queue, (cost + 1, (x + direction[0], y + direction[1]), direction))
        turn_right = rotate_clockwise(direction)
        turn_left = rotate_anticlockwise(direction)
        heapq.heappush(queue, (cost + 1000, pos, turn_right))
        heapq.heappush(queue, (cost + 1000, pos, turn_left))

def part_two(walls, start, end, width, height):
    best_cost = bfs(walls, start, end)
    
    initial_direction = (1, 0)
    queue = []
    prev_state = []
    heapq.heappush(queue, (0, start, initial_direction))
    visited = set()
    while queue:
        cost, pos, direction = heapq.heappop(queue)
        if cost > best_cost:
            break
        
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))
        
        x, y = pos
        if (x + direction[0], y + direction[1]) not in walls:
            prev_state.append((cost + 1, (x, y), (x + direction[0], y + direction[1]), direction, direction))
            heapq.heappush(queue, (cost + 1, (x + direction[0], y + direction[1]), direction))
        turn_right = rotate_clockwise(direction)
        turn_left = rotate_anticlockwise(direction)
        prev_state.append((cost + 1000, pos, pos, direction, turn_right))
        prev_state.append((cost + 1000, pos, pos, direction, turn_left))
        heapq.heappush(queue, (cost + 1000, pos, turn_right))
        heapq.heappush(queue, (cost + 1000, pos, turn_left))
    
    best_prev_state = defaultdict(list)
    for state in prev_state:
        best_prev_state[(state[2], state[4])].append((state[0], state[1], state[3]))

    for state in best_prev_state:
        prevs = best_prev_state[state]
        best_prev_cost = prevs[0][0]
        best_prevs = []
        for prev in prevs:
            if prev[0] < best_prev_cost:
                best_prev_cost = prev[0]
                best_prevs = [prev]
            elif prev[0] == best_prev_cost:
                best_prevs.append(prev)
        best_prev_state[state] = best_prevs
    
    seen_nodes = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direction in directions:
        seen = set()
        end_state = (end, direction)
        queue = [end_state]
        while queue != []:
            state = queue.pop(0)
            seen.add(state)
            if state in best_prev_state:
                for prev in best_prev_state[state]:
                    if prev not in seen:
                        seen.add(prev)
                        seen_nodes.add(prev[1])
                        queue.append((prev[1], prev[2]))
            

    return len(seen_nodes)


def main():
    lines = parse_input(16, is_live=1)

    walls = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            elif char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
    
    print(part_one(walls, start, end))
    print(part_two(walls, start, end, len(lines[0]), len(lines)))

if __name__ == "__main__":
    main()

