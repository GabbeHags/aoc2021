from collections import Counter


class FishCollection:

    def __init__(self, fishys: list[int]):
        self.fishy_count = Counter(fishys)

    def next(self):
        for i in range(0, 10, 1):
            ic = self.fishy_count[i]
            self.fishy_count[i-1] = ic
        self.fishy_count[6] += self.fishy_count[-1]
        self.fishy_count[8] = self.fishy_count[-1]
        self.fishy_count[-1] = 0


def part_a(fishys: FishCollection):
    DAY_TO_CALC = 80
    for _ in range(DAY_TO_CALC):
        fishys.next()
    return sum(fishys.fishy_count.values())


def part_b(fishys: FishCollection):
    DAY_TO_CALC = 256
    for _ in range(DAY_TO_CALC):
        fishys.next()
    return sum(fishys.fishy_count.values())


def main() -> tuple:
    with open("../input.txt") as f:
        fishys = [int(day) for day in f.read().split(",")]
        fishys_a = FishCollection(fishys)
        fishys_b = FishCollection(fishys)
    return part_a(fishys_a), part_b(fishys_b)


if __name__ == '__main__':
    import time
    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
