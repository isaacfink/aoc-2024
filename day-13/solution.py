import time
import re
import numpy as np

start = time.time()

only_digits = re.compile(r"\d+")


def get_content(file_path):
    lines: list[list[int]] = []
    with open(file_path, "r") as f:
        lines = [
            [int(y) for y in only_digits.findall(x)] for x in f.read().split("\n\n")
        ]

    return lines


def part_one(file_path):
    machines = get_content(file_path)
    total = 0
    for machine in machines:
        ax, ay, bx, by, prize_x, prize_y = machine
        total_price = 0
        for i in range(100):
            total_b_needed_x = (prize_x - (i * ax)) / bx
            total_b_needed_y = (prize_y - (i * ay)) / by

            if (
                total_b_needed_x.is_integer()
                and total_b_needed_y.is_integer()
                and total_b_needed_x == total_b_needed_y
            ):
                price = (3 * i) + (total_b_needed_x)
                if total_price == 0:
                    total_price = price
                else:
                    total_price = min(total_price, (3 * i) + (total_b_needed_y))
        total += total_price
    return int(total)


def part_two(file_path):
    machines = get_content(file_path)
    total = 0
    tokens_cost = np.array([3, 1])

    for machine in machines:

        A = np.array([[machine[0], machine[2]], [machine[1], machine[3]]])
        y = np.array([10000000000000 + machine[4], 10000000000000 + machine[5]])
        try:
            x = np.linalg.solve(A, y)
        except np.linalg.LinAlgError as e:
            print(e)  # never happens for our input
            continue
        # check if x is whole numbers and larger than 0
        x_rounded = np.round(x)
        x_is_valid = np.all(0 <= x_rounded) and np.allclose(
            x, x_rounded, rtol=1e-14, atol=1e-8
        )  # need to adjust the defaults rtol=1e-9, atol=1e-5, because they were too sensitive for large values in y
        if not x_is_valid:
            continue
        total += int(np.dot(tokens_cost, x_rounded.reshape(-1, 1)).item())

    return total


print(part_one("test.txt"))  # 480
print(part_one("input.txt"))  # 33,481

print(part_two("test.txt"))  # 875,318,608,908
print(part_two("input.txt"))  # 92,572,057,880,885

end = time.time()
elapsed = end - start

hours, remainder = divmod(elapsed, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Time: {int(hours):02}:{int(minutes):02}:{seconds:.2f}")
