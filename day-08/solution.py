import time
from typing import List
import itertools

start = time.time()


def get_content(file_path):
    lines: List[List[str]] = []
    with open(file_path, "r") as f:
        lines = [[y for y in x.strip()] for x in f.readlines()]

    return lines


def create_antennas(input: list[list[str]]):
    antennas: dict[str, list[tuple[int, int]]] = {}

    for row_idx, row in enumerate(input):
        for col_idx, col in enumerate(row):
            is_antenna = col not in ".#"
            if is_antenna:
                if col in antennas:
                    antennas[col].append((row_idx, col_idx))
                else:
                    antennas[col] = [(row_idx, col_idx)]

    return antennas


def get_antinodes(
    antennas: dict[str, list[tuple[int, int]]],
    content: list[list[str]],
    count_all=False,
):
    found_targets = set()
    for antenna in antennas.values():
        for first, second in itertools.combinations(antenna, 2):
            diff = (first[0] - second[0], first[1] - second[1])
            dirs = [
                (first[0] + diff[0], first[1] + diff[1]),
                (second[0] - diff[0], second[1] - diff[1]),
                (first[0], first[1]) if count_all else None,
                (second[0], second[1]) if count_all else None,
            ]

            if count_all:

                while is_in_bounds(first, len(content)):
                    first = (first[0] + diff[0], first[1] + diff[1])
                    dirs.append(first)

                while is_in_bounds(second, len(content)):
                    second = (second[0] - diff[0], second[1] - diff[1])
                    dirs.append(second)

            for dir in dirs:
                if dir is not None and is_in_bounds(dir, len(content)):
                    found_targets.add(f"{dir[0]}-{dir[1]}")
    return found_targets


def is_in_bounds(point: tuple[int, int], size: int):
    return all([point[0] >= 0, point[0] < size, point[1] >= 0, point[1] < size])


def part_one(file_path):
    content = get_content(file_path)

    antennas = create_antennas(content)
    found_targets = get_antinodes(antennas, content)

    return len(found_targets)


def part_two(file_path):
    content = get_content(file_path)

    antennas = create_antennas(content)
    found_targets = get_antinodes(antennas, content, True)

    return len(found_targets)


print(part_one("test.txt"))  # 14
print(part_one("input.txt"))  # 299
print(part_two("test.txt"))  # 34
print(part_two("input.txt"))  # 1032

end = time.time()
print(f"Time: {end - start}")
