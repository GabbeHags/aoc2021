def get_most_common(arr: list, pos: int):
    gamma_bit_count = 0
    epsilon_bit_count = 0
    for binary in arr:
        if binary[pos] == "1":
            gamma_bit_count += 1
        else:
            epsilon_bit_count += 1

    if gamma_bit_count >= epsilon_bit_count:
        return "1"
    else:
        return "0"


def flip(bit: str):
    if bit == "1":
        return "0"
    else:
        return "1"


def part_a(arr):
    gamma = ""
    epsilon = ""
    for pos in range(len(arr[0])):
        common = get_most_common(arr, pos)
        gamma += common
        epsilon += flip(common)
    return int(gamma, 2) * int(epsilon, 2)


def get_rating(arr: list, f: bool = False):
    bits_len = len(arr[0])
    result = arr[:]
    for i in range(bits_len):
        common = get_most_common(result, i)
        common = flip(common) if f else common
        result = [_b for _b in result if _b[i] == common]
        if len(result) == 1:
            break
    return result


def part_b(arr):
    oxygen = get_rating(arr[:])
    co2 = get_rating(arr[:], True)
    return int("".join(oxygen[0]), 2) * int("".join(co2[0]), 2)


def main() -> tuple:
    with open("../input.txt") as f:
        arr = [bits[:-1] for bits in f]
    return part_a(arr), part_b(arr)


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
