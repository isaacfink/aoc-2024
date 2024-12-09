import time
from alive_progress import alive_bar

start = time.time()


def get_content(file_path):
    blocks: list[str] = []
    with open(file_path, "r") as f:
        for i, char in enumerate(f.read()):
            for j in range(int(char)):
                if i % 2 == 0:
                    blocks.append(str(int(i / 2)))
                else:
                    blocks.append(".")

    return blocks


def find_last_digit_position(s: list[str]) -> int:
    for i, char in enumerate(s[::-1]):
        if char.isdigit():
            return len(s) - i - 1

    return -1


def part_one(file_path):
    content = get_content(file_path)

    last_empty_pos = 0

    for i in range(len(content) - 1, 0, -1):
        if content[i].isdigit():
            try:
                empty_index = content.index(".", last_empty_pos, i)
                content[i], content[empty_index] = content[empty_index], content[i]
                last_empty_pos = empty_index
            except ValueError:
                break

    return sum([int(x) * pos for pos, x in enumerate(content) if x != "."])


def part_two(file_path):
    content = get_content(file_path)

    last_empty_pos: dict[str, int] = {}

    def get_last_empty_pos(length: int):
        keys = list(last_empty_pos.keys())
        keys.sort()
        for k in keys[::-1]:
            if int(k) <= length:
                return last_empty_pos[k]

    def find_first_index(count: int, start=0, stop=None):
        split_array = content.copy()[start:stop]
        for index, char in enumerate(split_array):
            if char == "." and all(
                [x == "." for x in split_array[index : index + count]]
            ):
                return index + start
        return None

    i = len(content) - 1
    with alive_bar(len(content)) as bar:
        while i > 0:
            if content[i].isdigit():
                char_length = 1
                char = content[i]
                for j in range(i - 1, 0, -1):
                    if content[j] == char:
                        char_length += 1
                    else:
                        break

                empty_index = find_first_index(
                    char_length, get_last_empty_pos(char_length) or 0, i
                )
                if empty_index:
                    for x in range(char_length):
                        content[empty_index + x] = char
                        content[i - x] = "."
                    last_empty_pos[str(char_length)] = empty_index
                i -= char_length
                for _ in range(char_length):
                    bar()
            else:
                i -= 1
                bar()

    return sum([int(x) * pos for pos, x in enumerate(content) if x != "."])


print(part_one("test.txt"))  # 1928
print(part_one("input.txt"))  # 6,415,184,586,041
print(part_two("test.txt"))  # 2858
print(part_two("input.txt"))  # 6,436,819,084,274

end = time.time()
elapsed = end - start

hours, remainder = divmod(elapsed, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")
