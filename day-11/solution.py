from functools import cache
import time

start = time.time()


def get_content(file_path):
    with open(file_path, "r") as f:
        return [x for x in f.read().strip().split()]


@cache
def replace(stone: str) -> list[str]:
    if stone == "0":
        return ["1"]
    if len(stone) % 2 == 0:
        halfpoint = len(stone) // 2
        first, second = stone[:halfpoint], stone[halfpoint:]
        return [str(int(first)), str(int(second))]
    return [str(int(stone) * 2024)]


def flatten_list(input: list[list[str]]) -> list[str]:
    return [item for sublist in input for item in sublist]


@cache
def solve_recursive(stone: str, iteration: int) -> int:
    if iteration == 0:
        return 1

    new_stones = replace(stone)

    return sum([solve_recursive(s, iteration - 1) for s in new_stones])


def solve(file_path: str, iterations: int):
    content = get_content(file_path)
    return sum([solve_recursive(s, iterations) for s in content])


def part_one(file_path):
    return solve(file_path, 25)


def part_two(file_path):
    return solve(file_path, 75)


print(part_one("test.txt"))  # 55312
print(part_one("input.txt"))  # 199986
print(part_two("input.txt"))  # 236804088748754

end = time.time()
elapsed = end - start

hours, remainder = divmod(elapsed, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")
