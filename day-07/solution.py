import time
from typing import List, Tuple

start = time.time()


def get_content(file_path):
    lines: List[Tuple[int, List[int]]] = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            total, operators = line.split(":")
            operators_int = [int(x) for x in operators.split()]
            lines.append((int(total), operators_int))

    return lines


def calculate_possible_totals(
    operators, total, operator, desired_total, allow_concat=False
):
    if len(operators) == 0:
        if total == desired_total:
            return True
        return False

    new_total = total
    current_number, *rest = operators
    if operator == "+":
        new_total += current_number
    elif operator == "*":
        new_total *= current_number
    elif operator == "|":
        new_total = int(str(total) + str(current_number))

    if new_total > desired_total:
        return False

    return (
        calculate_possible_totals(rest, new_total, "*", desired_total, allow_concat)
        or calculate_possible_totals(rest, new_total, "+", desired_total, allow_concat)
        or (
            allow_concat
            and calculate_possible_totals(
                rest, new_total, "|", desired_total, allow_concat
            )
        )
    )


def part_one(file_path):
    content = get_content(file_path)
    total = 0
    for line in content:
        current, *res = line[1]
        if calculate_possible_totals(
            res, current, "*", line[0]
        ) or calculate_possible_totals(res, current, "+", line[0]):
            total += line[0]

    return total


def part_two(file_path):
    content = get_content(file_path)
    total = 0
    for line in content:
        current, *res = line[1]
        if (
            calculate_possible_totals(res, current, "*", line[0], True)
            or calculate_possible_totals(res, current, "+", line[0], True)
            or calculate_possible_totals(res, current, "|", line[0], True)
        ):
            total += line[0]

    return total


print(part_one("test.txt"))  # 3749
print(part_one("input.txt"))  # 6083020304036
print(part_two("test.txt"))  # 11387
print(part_two("input.txt"))  # 59002246504791

end = time.time()
print(f"Time: {end - start}")
