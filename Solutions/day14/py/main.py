from collections import Counter

rules = {}


def do(inp, max_steps):
    steps = 0
    counter = Counter()
    for i in range(len(inp)):
        if i + 1 < len(inp):
            counter[inp[i] + inp[i + 1]] += 1
    while steps < max_steps:
        new_counter = Counter()
        for k, v in counter.items():
            if k in rules:
                new_counter[k[0] + rules[k]] += v
                new_counter[rules[k] + k[1]] += v
            else:
                new_counter[k] += v
        counter = new_counter
        steps += 1
    res_counter = Counter()
    for k, v in counter.items():
        res_counter[k[0]] += v
    res_counter[inp[-1]] += 1
    return max(res_counter.values()) - min(res_counter.values())


def part_a(inp: str):
    return do(inp, 10)


def part_b(inp: str):
    return do(inp, 40)


def main(file) -> tuple:
    with open(file) as f:
        inp = f.readline().strip()
        f.readline()
        for rule in f.read().strip().split("\n"):
            l, r = rule.split(" -> ")
            rules[l] = r
    return part_a(inp), part_b(inp)


if __name__ == '__main__':
    import time
    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
