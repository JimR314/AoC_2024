from AoC_Lib import parse_input

def get_tokens(machine):
    # Solve following 2 linear equations:
    # ax + by = m
    # cx + dy = n
    
    # x = (n - dy) / c
    # a(n - dy) + bcy = cm
    # bcy - ady = cm - an

    a, c = machine[0]
    b, d = machine[1]
    m, n = machine[2]

    y = (c * m - a * n) / (b * c - a * d)
    x = (n - d * y) / c

    if x.is_integer() and y.is_integer():
        return 3*x + y
    return 0

def part_one(machines):
    total_tokens = 0

    for machine in machines:
        total_tokens += get_tokens(machine)
    
    return total_tokens

def part_two(machines):
    total_tokens = 0

    for machine in machines:
        machine[2] = (10000000000000 + machine[2][0], 10000000000000 + machine[2][1])
        total_tokens += get_tokens(machine)
    
    return total_tokens

def main():
    lines = parse_input(13, is_live=1)
    machines = []
    machine = []
    for m in lines:
        if m == "":
            continue

        p1, p2 = m.split(',')
        if m[0] == 'B':
            v1 = int(p1.split('+')[1])
            v2 = int(p2.split('+')[1])
            machine.append((v1, v2))
        else:
            v1 = int(p1.split('=')[1])
            v2 = int(p2.split('=')[1])
            machine.append((v1, v2))
            machines.append(machine)
            machine = []

    print(part_one(machines))
    print(part_two(machines))

if __name__ == "__main__":
    main()