
def part_a(arr: list[tuple[str, int]]) -> int:
    horizontal = 0
    depth = 0
    for cmd, num in arr:
        if cmd == "forward":
            horizontal += num
        elif cmd == "up":
            depth -= num
        elif cmd == "down":
            depth += num
    return horizontal * depth


def part_b(arr) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for cmd, num in arr:
        if cmd == "forward":
            horizontal += num
            depth += (num * aim)
        elif cmd == "up":
            aim -= num
        elif cmd == "down":
            aim += num
    return horizontal * depth


def main() -> tuple[int, int]:
    with open("../input.txt") as f:
        arr = []
        for line in f:
            cmd, num = line.split(" ")
            arr.append((cmd, int(num)))

    return part_a(arr), part_b(arr)


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
