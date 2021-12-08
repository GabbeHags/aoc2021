def minus(left: str, right: str):
    if len(left) >= len(right):
        str_short = right
        str_long = left
    else:
        str_short = left
        str_long = right
    for c in str_short:
        if c in str_long:
            str_long = str_long.replace(c, "")
    return str_long


class Line:

    def __init__(self, long, short):
        self.long: list[str] = long
        self.short: list[str] = short
        self.nums = self.gen_num_mapping()

    def gen_num_mapping(self) -> dict[int, str]:
        char_mapping: dict[str, str] = {char: "" for char in "abcdefg"}
        nums: dict[int, str] = {n: "" for n in range(0, 8)}
        for n in self.long:
            if len(n) == 2:
                nums[1] = n
            elif len(n) == 3:
                nums[7] = n
            elif len(n) == 4:
                nums[4] = n
            elif len(n) == 7:
                nums[8] = n

        # map "a"
        for c in nums[7]:
            if c not in nums[1]:
                char_mapping["a"] = c
        # get num 9 and char e
        for l in self.long:
            if len(l) == 6:
                if minus(l, nums[8]) in minus(minus(nums[8], nums[7]), nums[4]):  # get num 9 and char e
                    nums[9] = l
                    char_mapping["e"] = minus(l, nums[8])
                elif minus(nums[8], l) in nums[1]:  # get char c and num 6
                    char_mapping["c"] = minus(nums[8], l)
                    nums[6] = l
                    char_mapping["f"] = minus(nums[1], char_mapping["c"])

        # get char g
        char_mapping["g"] = minus(minus(nums[4], nums[8]), char_mapping["a"] + char_mapping["e"])

        # get num 0 and char d and char b
        for l in self.long:
            if len(l) == 6 and l != nums[6] and l != nums[9]:
                nums[0] = l
                char_mapping["d"] = minus(l, nums[8])
                _b = "".join(char_mapping.values())
                char_mapping["b"] = minus(nums[0], _b)

        # get num 3
        for l in self.long:
            if len(l) == 5:
                if minus(minus(nums[7], l), char_mapping["g"] + char_mapping["d"]) == "":
                    nums[3] = l
                elif minus(l, char_mapping["a"] + char_mapping["b"] + char_mapping["d"] + char_mapping["f"] + char_mapping["g"]) == "":
                    nums[5] = l
                elif minus(l, char_mapping["a"] + char_mapping["c"] + char_mapping["d"] + char_mapping["e"] + char_mapping["g"]) == "":
                    nums[2] = l

        return nums

    def decode_num(self, decode) -> str:
        for (num, num_s) in self.nums.items():
            if sorted(decode) == sorted(num_s):
                return str(num)

    def __repr__(self):
        return f"{self.long} | {self.short}"


def part_a(lines) -> int:
    acc = 0
    for line in lines:
        acc += sum([len(u) == 2 or len(u) == 4 or len(u) == 3 or len(u) == 7 for u in line.short])
    return acc


def part_b(lines) -> int:
    _sum = 0
    for line in lines:
        s = ""
        for num in line.short:
            s += line.decode_num(num)
        _sum += int(s)
    return _sum


def main(file) -> tuple:
    lines = []

    with open(file) as f:
        for line in f:
            long, short = line.split(" | ")
            lines.append(Line(long.split(" "), [c.removesuffix("\n") for c in short.split(" ")]))
    return part_a(lines), part_b(lines)


if __name__ == '__main__':
    import time
    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
