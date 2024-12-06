import time

start = time.time()


def get_content(file_path):
    with open(file_path, "r") as f:
        return [[j for j in i] for i in [i for i in f.read().split("\n")]]


dir_markings = ["U", "R", "D", "L"]


def get_total_positions(content):
    current_pos = [(i, j.index("^")) for i, j in enumerate(content) if "^" in j][0]
    first_pos = (current_pos[0], current_pos[1])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = dirs[0]

    def is_in_range(pos):
        return 0 <= pos[0] < len(content) and 0 <= pos[1] < len(content[0])

    def turn_right():
        cur_index = dirs.index(dir)
        return dirs[(cur_index + 1) % len(dirs)]

    is_in_loop = False

    stepped_over = []

    while is_in_range(current_pos) and not is_in_loop:
        next_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])
        if dir_markings[dirs.index(dir)] in content[current_pos[0]][current_pos[1]]:
            is_in_loop = True
            break

        stepped_over.append(current_pos)
        if content[current_pos[0]][current_pos[1]] in ".^":
            content[current_pos[0]][current_pos[1]] = dir_markings[dirs.index(dir)]
        else:
            content[current_pos[0]][current_pos[1]] += dir_markings[dirs.index(dir)]

        if not is_in_range(next_pos):
            break

        if content[next_pos[0]][next_pos[1]] == "#":
            dir = turn_right()
        else:
            current_pos = next_pos

    return (
        sum(1 if all(z in dir_markings for z in y) else 0 for x in content for y in x),
        is_in_loop,
        stepped_over,
        first_pos,
    )


def part_one(file_path):
    content = get_content(file_path)

    return get_total_positions(content)[0]


def part_two(file_path):
    content = get_content(file_path)

    total = 0

    _, _, stepped_over, first_pos = get_total_positions(content)

    stepped_over_unique = list(set(stepped_over))

    for j, i in enumerate(stepped_over_unique):
        if i == first_pos:
            continue
        copy = get_content(file_path)
        copy[i[0]][i[1]] = "#"
        print(f"Trying {j}/{len(stepped_over)}")
        if get_total_positions(copy)[1]:
            total += 1
    return total


print(part_one("test.txt"))  # 41
print(part_one("input.txt"))  # 5162
print(part_two("test.txt"))  # 6
print(part_two("input.txt"))  # 1909

end = time.time()
print(f"Time: {end - start}")
