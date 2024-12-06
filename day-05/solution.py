def part_one(file_path):
    with open(file_path) as f:
        raw_content = f.read().split("\n\n")
        rules = [
            (int(i.split("|")[0]), int(i.split("|")[1]))
            for i in raw_content[0].split("\n")
        ]

        page_rows = [[int(x) for x in i.split(",")] for i in raw_content[1].split("\n")]

        def get_page_value(page):
            pages_hash = {x: i for i, x in enumerate(page)}
            is_in_order = True
            for i in rules:
                first = pages_hash.get(i[0])
                second = pages_hash.get(i[1])

                if first is not None and second is not None:
                    if first > second:
                        is_in_order = False
                        break
            if is_in_order:
                return page[len(page) // 2]
            else:
                return 0

        return sum([get_page_value(i) for i in page_rows])


def part_two(file_path):
    with open(file_path) as f:
        raw_content = f.read().split("\n\n")
        rules = {x for x in raw_content[0].split("\n")}

        page_rows = [[int(x) for x in i.split(",")] for i in raw_content[1].split("\n")]

        def sort_page(page):
            is_in_order = False
            has_changed = False
            new_page = page.copy()

            while not is_in_order:
                is_in_order = True
                for i in range(1, len(new_page)):
                    if f"{new_page[i]}|{new_page[i - 1]}" in rules:
                        new_page[i], new_page[i - 1] = new_page[i - 1], new_page[i]
                        is_in_order = False
                        has_changed = True
            return new_page[len(new_page) // 2] if has_changed else 0

        return sum([sort_page(i) for i in page_rows])


print(part_one("test.txt"))  # 143
print(part_one("input.txt"))  # 3608
print(part_two("test.txt"))  # 123
print(part_two("input.txt"))  # 4922
