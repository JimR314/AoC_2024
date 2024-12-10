from AoC_Lib import parse_input

def part_one(line):
    sum = 0
    l = 0
    sizes = []
    gaps = []
    num_blocks = (len(line) + 1) // 2

    for i in range(len(line)):
        if i % 2 != 0:
            gaps.append(int(line[i]))
        else:
            l += int(line[i])
            sizes.append(int(line[i]))
    

    pos = 0
    block = 0
    rear_block = num_blocks - 1
    for i, char in enumerate(line):
        for j in range(int(char)):
            # print(f"i: {i}, j: {j}, pos: {pos}, block: {block}, rear_block: {rear_block}, sum: {sum}")
            if i % 2 == 0:
                sum += block * pos
                pos += 1
                if j == int(char) - 1:
                    block += 1
            else:
                sum += rear_block * pos
                pos += 1
                sizes[rear_block] -= 1
                if sizes[rear_block] == 0:
                    rear_block -= 1
            
            if pos >= l:
                break
        if pos >= l:
            break
    return sum


def part_two(line):
    # Parse the input line into alternating file lengths and free lengths
    lengths = [int(x) for x in line.strip()]
    # lengths[0] is file length, lengths[1] is free length, lengths[2] file, lengths[3] free, and so forth.
    
    # Build the disk layout (list of chars)
    # Each file gets an ID starting from 0
    disk = []
    file_id = 0
    i = 0
    while i < len(lengths):
        # Even index: file length
        f_len = lengths[i]
        # Append file blocks with the current file_id
        if f_len > 0:
            # Convert file_id to a single character. The examples show single-digit IDs,
            # but we must be careful if file_id > 9. The examples given don't seem to exceed single digit.
            # However, the puzzle's example might. We can store them as strings of digits.
            # It's safer to just store them as their string representation of the file_id.
            # If the puzzle input is large and has more than 10 files, we still just store the integer as a string.
            # The checksum calculation will parse it back to int anyway.
            fid_str = str(file_id)
            disk.extend([fid_str] * f_len)
        
        # Increment file_id after each file length
        file_id += 1
        
        # If there is a corresponding free length, it should be at i+1
        if i+1 < len(lengths):
            free_len = lengths[i+1]
            if free_len > 0:
                disk.extend(['.'] * free_len)
        i += 2  # Move to the next pair
    
    # The number of files is file_id because we incremented after each file length
    # The highest file_id used is file_id-1
    max_file_id = file_id - 1
    
    # Function to find the positions of a given file_id in the disk
    def find_file_positions(fid):
        # Return start_index, length, and positions list
        fid_str = str(fid)
        positions = [idx for idx, block in enumerate(disk) if block == fid_str]
        if not positions:
            return None, 0, []
        return positions[0], len(positions), positions
    
    # Attempt to move each file in order of decreasing file ID number
    for fid in range(max_file_id, -1, -1):
        if fid%100 == 0: print(fid)
        start_idx, flen, positions = find_file_positions(fid)
        if flen == 0:
            # File not found (might have length 0), skip
            continue
        
        # Find a suitable free space run to the left of start_idx
        # We want the leftmost run of '.' of length >= flen that ends before start_idx
        # We'll scan from the left up to start_idx - 1
        left_limit = start_idx
        best_run_start = None
        best_run_length = 0
        
        # Scan for contiguous '.' runs
        run_start = None
        run_length = 0
        for idx in range(left_limit):
            if disk[idx] == '.':
                if run_start is None:
                    run_start = idx
                    run_length = 1
                else:
                    run_length += 1
            else:
                # End of a run
                if run_start is not None:
                    # Check if this run is big enough
                    if run_length >= flen:
                        best_run_start = run_start
                        best_run_length = run_length
                        break  # We found the leftmost suitable run
                    run_start = None
                    run_length = 0
        
        # Check at the end if we ended with a run
        if run_start is not None and run_length >= flen and best_run_start is None:
            # If we finished scanning and found a suitable run at the end of scanning
            best_run_start = run_start
            best_run_length = run_length
        
        # If we found a suitable run, move the file there
        if best_run_start is not None:
            # Move file blocks into that run
            # Overwrite the free space with the file blocks
            for offset in range(flen):
                disk[best_run_start + offset] = str(fid)
            # The original file blocks become '.'
            for pos in positions:
                disk[pos] = '.'
    
    # Compute the checksum
    checksum = 0
    for idx, block in enumerate(disk):
        if block != '.':
            # block is the file_id as a string, convert to int
            fid = int(block)
            checksum += idx * fid
    
    return checksum


def main():
    lines = parse_input(9, is_live=1)

    print(part_one(lines[0]))
    print(part_two(lines[0]))

if __name__ == "__main__":
    main()