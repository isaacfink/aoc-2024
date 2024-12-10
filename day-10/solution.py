import time

start = time.time()

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def get_content(file_path):
    with open(file_path, "r") as f:
        return [[int(y) for y in x.strip()] for x in f.readlines()]


def is_out_of_bounds(x: int, y: int, size: int):
    return x < 0 or y < 0 or x >= size or y >= size


def get_trails(
    dir: tuple[int, int],
    current_number: int,
    row: int,
    col: int,
    end_points: list[str],
    map: list[list[int]],
) -> list[str]:

    new_row, new_col = (row + dir[0], col + dir[1])
    if is_out_of_bounds(new_row, new_col, len(map)):
        return end_points

    if map[new_row][new_col] == current_number + 1:
        if current_number + 1 == 9:
            return end_points + [f"{new_row}-{new_col}"]
        return [
            trails
            for trails_list in [
                get_trails(x, current_number + 1, new_row, new_col, end_points, map)
                for x in dirs
            ]
            for trails in trails_list
        ]

    return end_points


def get_all_trails(map: list[list[int]]):
    all_trails: list[list[str]] = []

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col == 0:
                all_trails.append(
                    [
                        trails
                        for trails_list in [
                            get_trails(x, 0, row_idx, col_idx, [], map) for x in dirs
                        ]
                        for trails in trails_list
                    ]
                )

    return all_trails


def part_one(file_path):
    map = get_content(file_path)
    return sum([len(set(x)) for x in get_all_trails(map)])


def part_two(file_path):
    map = get_content(file_path)

    return sum([len(x) for x in get_all_trails(map)])


print(part_one("test.txt"))  # 36
print(part_one("input.txt"))  # 582
print(part_two("test.txt"))  # 81
print(part_two("input.txt"))  # 1302

end = time.time()
elapsed = end - start

hours, remainder = divmod(elapsed, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")
