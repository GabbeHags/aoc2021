def part_a(arr) -> int:
    count = 0
    prev = None
    for curr in arr:
        if prev is not None and prev < curr:
            count += 1
        prev = curr
    return count


def part_b(arr) -> int:
    prev = None
    count = 0
    for i in range(len(arr)):
        arr_slice = arr[i:i + 3]
        curr = sum(arr_slice)
        if len(arr_slice) == 3 and prev is not None and prev < curr:
            count += 1
        prev = curr
    return count


def main() -> tuple[int, int]:
    with open("../input.txt") as f:
        arr = [int(line) for line in f.read().split("\n") if line.isdigit()]
    return part_a(arr), part_b(arr)


if __name__ == '__main__':
    import time
    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
