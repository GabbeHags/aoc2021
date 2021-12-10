from collections import deque

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

reverse_pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}


class Line:

    def __init__(self, l: str):
        self.line = l
        self.que: deque[str] = deque()

    def illegal_checker(self) -> str or None:
        for c in self.line:
            if c in pairs:
                self.que.append(c)
            else:
                if reverse_pairs[c] == self.que[-1]:
                    self.que.pop()
                else:
                    self.que = []
                    return c

    def fix_missing_closings(self) -> bool:
        if len(self.que) == 0:
            if self.illegal_checker() is not None:
                # self.line = ""
                return False
            elif len(self.que) == 0:
                return True
        # for _ in range(len(self.que)):
        #     self.line += pairs[self.que.pop()]
        return True


def illegal_score(s: str) -> int:
    if s == ")": return 3
    if s == "]": return 57
    if s == "}": return 1197
    if s == ">": return 25137


def complete_score(s: str) -> int:
    if s == ")": return 1
    if s == "]": return 2
    if s == "}": return 3
    if s == ">": return 4


def part_a(lines: list[Line]):
    acc = 0
    for line in lines:
        if (char := line.illegal_checker()) is not None:
            acc += illegal_score(char)
    return acc


def part_b(lines: list[Line]):
    conuts = []
    for line in lines:
        if line.fix_missing_closings():
            acc = 0
            for i in range(len(line.que)):
                acc *= 5
                acc += complete_score(pairs[line.que.pop()])
            conuts.append(acc)
    return sorted(conuts)[len(conuts) // 2]


def main(file) -> tuple:
    with open(file) as f:
        lines = [Line(line.removesuffix("\n")) for line in f]
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
