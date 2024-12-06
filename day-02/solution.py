def get_direction(one, two):
    return one < two


def test_reading(array):
    is_going_up = get_direction(array[0], array[1])
    is_safe_local = True
    for i in range(1, len(array)):
        diff = abs(array[i] - array[i - 1])
        if get_direction(array[i - 1], array[i]) != is_going_up:
            is_safe_local = False
            break
        if diff < 1 or diff > 3:
            is_safe_local = False
            break
    return is_safe_local


def part_one(file_path):
    total_safe = 0
    with open(file_path, "r") as f:
        for line in f:
            readings = list(map(int, line.split()))
            is_safe = test_reading(readings)

            if is_safe:
                total_safe += 1

    return total_safe


def get_all_possible_without_one(array):
    res = [array[:i] + array[i + 1 :] for i in range(len(array))]
    res.append(array)
    return res


def part_two(file_path):
    total_safe = 0
    with open(file_path, "r") as f:
        for line in f:
            readings = list(map(int, line.split()))
            all_readings = get_all_possible_without_one(readings)
            for i in all_readings:
                if test_reading(i):
                    total_safe += 1
                    break

    return total_safe


print(part_one("test.txt"))  # 2
print(part_one("input.txt"))  # 549
print(part_two("test.txt"))  # 4
print(part_two("input.txt"))  # 589
