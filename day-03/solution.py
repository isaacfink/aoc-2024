import re

multiplier_pattern = re.compile("mul\\((\\d+),(\\d+)\\)")


def part_one(file_path):
    total = 0
    with open(file_path, "r") as f:
        content = f.read()
        matches = re.findall(multiplier_pattern, content)
        for i in matches:
            total += int(i[0]) * int(i[1])
    return total


def part_two(file_path):
    total = 0
    with open(file_path, "r") as f:
        content = f.read()

        new_text = content

        while "don't()" in new_text:
            index = new_text.index("don't()")
            next_index = new_text.index("do()", index)
            new_text = new_text[:index] + new_text[next_index + 4 :]

        matches = multiplier_pattern.finditer(new_text)

        for i in matches:
            total += int(i.group(1)) * int(i.group(2))
    return total


print(part_one("test.txt"))  # 161
print(part_one("input.txt"))  # 159892596
print(part_two("test2.txt"))  # 48
print(part_two("input.txt"))  # 92626942
