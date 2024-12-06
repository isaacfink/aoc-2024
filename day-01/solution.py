def part_one(file_path):
    array_1 = []
    array_2 = []

    total_diff = 0
    with open(file_path, "r") as f:
        for line in f:
            array_1.append(int(line.split()[0]))
            array_2.append(int(line.split()[1]))

    array_1 = sorted(array_1)
    array_2 = sorted(array_2)

    for j, k in zip(array_1, array_2):
        total_diff += abs(j - k)

    return total_diff


def part_two(file_path):
    array_1 = []
    array_2 = []

    similarity_score = 0
    with open(file_path, "r") as f:
        for line in f:
            array_1.append(int(line.split()[0]))
            array_2.append(int(line.split()[1]))

    array_1 = sorted(array_1)
    array_2 = sorted(array_2)

    for i in array_1:
        similarity_score += i * len(list(filter(lambda x: x == i, array_2)))

    return similarity_score


print(part_one("test.txt"))  # 11
print(part_one("input.txt"))  # 1651298
print(part_two("test.txt"))  # 31
print(part_two("input.txt"))  # 21306195
