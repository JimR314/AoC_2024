def parse_input(day: int, is_live: bool = True) -> list[str]:
    lines = []
    input_folder = "my_inputs" if is_live else "test_inputs"
    file_path = f"./inputs/{input_folder}/day_{day}.txt"
    with open(file_path, "r") as f:
        l = f.readlines()
        for line in l:
            lines.append(line.strip())
        return lines