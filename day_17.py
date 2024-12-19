from AoC_Lib import parse_input

def get_combo_operand(operand, A, B, C):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    print("Error: invalid operand ", operand)    

def part_one(instructions, A, B, C):
    output = ""

    counter = 0
    while counter < len(instructions):
        opcode, operand = instructions[counter]
        if opcode == 0:
            num = A
            denom = 2 ** get_combo_operand(operand, A, B, C)
            truncated_frac = num // denom
            A = truncated_frac
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = get_combo_operand(operand, A, B, C) % 8
        elif opcode == 3:
            if A == 0:
                counter += 1
            else:
                counter = operand
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output += str(get_combo_operand(operand, A, B, C) % 8) + ","
        elif opcode == 6:
            num = A
            denom = 2 ** get_combo_operand(operand, A, B, C)
            truncated_frac = num // denom
            B = truncated_frac
        elif opcode == 7:
            num = A
            denom = 2 ** get_combo_operand(operand, A, B, C)
            truncated_frac = num // denom
            C = truncated_frac
        
        if opcode != 3:
            counter += 1
    

    return output[:-1]

def part_two(instructions, A, B, C):
    vals = []
    for (opcode, operand) in instructions:
        vals.append(opcode)
        vals.append(operand)

    # Maths behind my input

    # 2,4: B = A mod 8
    # 1,5: B = B xor 5
    # 7,5: C = A // (2^B)
    # 0,3: A = A // 8
    # 1,6: B = B xor 6
    # 4,3: B = B xor C
    # 5,5: output B
    # 3,0

    # a, b, c
    # a, a%8, c
    # a, (a%8) xor 5, c
    # a, (a%8) xor 5, a // (2 ^ ((a%8) xor 5))
    # a // 8, (a%8) xor 5, a // (2 ^ ((a%8) xor 5))
    # a // 8, (a%8) xor 3, a // (2 ^ ((a%8) xor 5))
    # a // 8, ((a%8) xor 3) xor (a // (2 ^ ((a%8) xor 5))), a // (2 ^ ((a%8) xor 5))

    # B = ((a%8) xor 3) xor (a // (2 ^ ((a%8) xor 5)))
    # B = ((A % 8) ^ 3) ^ (A // (2 ** ((A % 8) ^ 5)))
    
    def forward_compute_b(A):
        return ((A % 8) ^ 3) ^ (A // (2 ** ((A % 8) ^ 5)))

    iteration_count = len(vals)
    current_possible_As = []
    for A_candidate in range(8):
        if forward_compute_b(A_candidate) == vals[-1]:
            current_possible_As.append(A_candidate)

    for i in range(iteration_count - 2, -1, -1):
        new_possible_As = []
        for A_next in current_possible_As:
            start_range = A_next * 8
            end_range = A_next * 8 + 7
            for A_candidate in range(start_range, end_range + 1):
                if forward_compute_b(A_candidate) % 8 == vals[i]:
                    new_possible_As.append(A_candidate)
        current_possible_As = new_possible_As
        if not current_possible_As:
            break

    if not current_possible_As:
        print("No solution found")
        return None

    A_initial = min(a for a in current_possible_As if a > 0)

    test_A = A_initial
    B = 0
    C = 0
    output_vals = []
    for _ in vals:
        B = forward_compute_b(test_A) % 8
        output_vals.append(B)
        test_A = test_A // 8

    # print("Found A_initial:", A_initial)
    # print("Expected:", vals)
    # print("Produced:", output_vals)

    return A_initial

def main():
    lines = parse_input(17, is_live=1)

    instructions = []
    for line in lines:
        if "Register" in line:
            if "A" in line:
                A = int(line.split(": ")[1])
            if "B" in line:
                B = int(line.split(": ")[1])
            if "C" in line:
                C = int(line.split(": ")[1])
        elif line == "":
            continue
        l = line.split(": ")[1].split(',')
        code = 1
        for i in range(len(l)):
            if code == 1:
                code = 0
            elif code == 0:
                instructions.append((int(l[i-1]), int(l[i])))
                code = 1

    print(part_one(instructions, A, B, C))
    print(part_two(instructions, A, B, C))

if __name__ == "__main__":
    main()