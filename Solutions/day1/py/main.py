def part_a(arr) -> int:
    count = 0
    for prev, curr in zip(arr, arr[1:]):
        if prev < curr:
            count += 1
    return count


def part_b(arr) -> int:
    return part_a([e1 + e2 + e3 for e1, e2, e3 in zip(arr, arr[1:], arr[2:])])


def main() -> tuple[int, int]:
    with open("../input.txt") as f:
        arr = [int(line) for line in f]
    return part_a(arr), part_b(arr)


if __name__ == '__main__':
    import time
    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
