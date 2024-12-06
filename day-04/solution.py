directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_content(file_path):
    with open(file_path, "r") as f:
        return [[j for j in i] for i in [i for i in f.read().split("\n")]]


def part_one(file_path):
    total = 0
    content = get_content(file_path)

    def traverse(row, col, direction, current_string):
        if row < 0 or col < 0:
            return 0
        try:
            current_string += content[row][col]
            if current_string == "XMAS":
                return 1
            elif "XMAS".startswith(current_string):
                return traverse(
                    row + direction[0], col + direction[1], direction, current_string
                )
            else:
                return 0

        except IndexError:
            return 0

    col_length = len(content[0])
    row_length = len(content)
    for row in range(row_length):
        for col in range(col_length):
            total += sum([traverse(row, col, x, "") for x in directions])
    return total


def part_two(file_path):
    total = 0
    content = get_content(file_path)

    col_length = len(content[0])
    row_length = len(content)

    additional_list = ["SM", "MS"]

    for row in range(1, row_length - 1):
        for col in range(1, col_length - 1):
            if content[row][col] == "A":
                first = f"{content[row -1][col-1]}{content[row+1][col+1]}"
                second = f"{content[row-1][col+1]}{content[row+1][col-1]}"

                if first in additional_list and second in additional_list:
                    total += 1

    return total


print(part_one("test.txt"))  # 18
print(part_one("input.txt"))  # 2530

print(part_two("test.txt"))  # 9
print(part_two("input.txt"))  # 1921
