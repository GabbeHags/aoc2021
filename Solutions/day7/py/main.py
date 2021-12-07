def part_a(positions):
    return min(sum(abs(i - n) for n in positions) for i in range(min(positions), max(positions)+1))


def part_b(positions):
    formula = lambda x: x * (x + 1) // 2
    return min(sum(formula(abs(i - n)) for n in positions) for i in range(min(positions), max(positions)+1))


def main(file_path) -> tuple:
    with open(file_path) as f:
        positions = [int(num) for num in f.read().split(",")]
    return part_a(positions), part_b(positions)


if __name__ == '__main__':
    import time
    file_path = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_path)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
