import time

start = time.time()


def get_content(file_path):
    lines: list[list[str]] = []
    with open(file_path, "r") as f:
        lines = [[y for y in x.strip()] for x in f.readlines()]

    return lines


#        up      right  down   left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(
    row_idx: int,
    col_idx: int,
    area: int,
    sides: int,
    map: list[list[str]],
    seen: set[str],
    count_corners=False,
):
    size = len(map)

    def is_in_bounds(point: tuple[int, int]):
        return 0 <= point[0] < size and 0 <= point[1] < size

    def is_dir_different(dir: tuple[int, int]):
        return not is_in_bounds(dir) or map[dir[0]][dir[1]] != map[row_idx][col_idx]

    def is_dir_same(dir: tuple[int, int]):
        return is_in_bounds(dir) and map[dir[0]][dir[1]] == map[row_idx][col_idx]

    seen.add(f"{row_idx},{col_idx}")
    area += 1
    all_neighbors = [(row_idx + x[0], col_idx + x[1]) for x in dirs]
    same_neighbors = [
        x
        for x in all_neighbors
        if is_in_bounds(x) and map[x[0]][x[1]] == map[row_idx][col_idx]
    ]

    if count_corners:
        # for part two we count corners instead of sides
        for dir in dirs:
            next_dir = dirs[(dirs.index(dir) + 1) % 4]
            side1 = (row_idx + dir[0], col_idx + dir[1])
            side2 = (row_idx + next_dir[0], col_idx + next_dir[1])
            side3 = (row_idx + dir[0] + next_dir[0], col_idx + dir[1] + next_dir[1])
            if is_dir_different(side1) and is_dir_different(side2):
                sides += 1
            elif is_dir_same(side1) and is_dir_same(side2) and is_dir_different(side3):
                sides += 1
    else:
        # for part one we count sides
        other_neighbors_count = len(all_neighbors) - len(same_neighbors)
        sides += other_neighbors_count

    for i in same_neighbors:
        if f"{i[0]},{i[1]}" in seen:
            continue
        sides, area = solve(i[0], i[1], area, sides, map, seen, count_corners)
    return sides, area


def solve_part(file_path: str, count_corners=False):
    map = get_content(file_path)

    seen: set[str] = set()

    total = 0
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if f"{row_idx},{col_idx}" in seen:
                continue
            corners, area = solve(row_idx, col_idx, 0, 0, map, seen, count_corners)
            total += corners * area
    return total


def part_one(file_path):
    return solve_part(file_path, False)


def part_two(file_path):
    return solve_part(file_path, True)


print(part_one("test2.txt"))  # 140
print(part_one("test1.txt"))  # 772
print(part_one("test.txt"))  # 1930
print(part_one("input.txt"))  # 1,319,878

print("part two")
print(part_two("test2.txt"))  # 80
print(part_two("test1.txt"))  # 436
print(part_two("test3.txt"))  # 236
print(part_two("test4.txt"))  # 368
print(part_two("test.txt"))  # 1206
print(part_two("input.txt"))  # 784,982

end = time.time()
elapsed = end - start

hours, remainder = divmod(elapsed, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")
