class Heights:

    def __init__(self, heights: list[list[int]]):
        self.heights = heights
        self.row_len = len(heights)
        self.col_len = len(heights[0])

    def adjacent(self, row, col) -> iter:
        if row < self.row_len-1:
            yield self.heights[row+1][col], (row+1, col)
        if row > 0:
            yield self.heights[row-1][col], (row-1, col)
        if col < self.col_len-1:
            yield self.heights[row][col+1], (row, col+1)
        if col > 0:
            yield self.heights[row][col-1], (row, col-1)

    def find_lowest_from(self, row, col, found=None):
        if found is None:
            found = set()
        lowest = self.heights[row][col]
        found.add((lowest, (row, col)))
        for val, (r, c) in self.adjacent(row, col):
            if val <= lowest and (val, (r, c)) not in found:

                self.find_lowest_from(r, c, found)

        # find min
        for val, (r, c) in found:
            if val < lowest:
                lowest = val
                row = r
                col = c
        return lowest, (row, col)

    def find_all_in_basin(self, val, row, col, found=None):
        if found is None:
            found = set()
        if (row, col) in found or val == 9:
            return found
        found.add((row, col))

        for v, (r, c) in self.adjacent(row, col):
            if self.heights[r][c] <= val:
                continue
            self.find_all_in_basin(v, r, c, found)
        return found


def part_a(heights: Heights):
    found = set()
    for row in range(heights.row_len):
        for col in range(heights.col_len):
            res = heights.find_lowest_from(row, col)
            found.add(res)
    result = 0
    for val, (_, _) in found:
        result += val + 1
    return result


def part_b(heights: Heights):
    basins = set()
    for row in range(heights.row_len):
        for col in range(heights.col_len):
            res = heights.find_lowest_from(row, col)
            basins.add(res)
    counts = []
    for (v, (r, c)) in basins:
        counts.append(len(heights.find_all_in_basin(v, r, c)))

    acc = 1
    for i in sorted(counts)[-3:]:
        acc *= i
    return acc


# from misc.misc_funcs import profile_func
#
# @profile_func
def main(file) -> tuple:
    heights: list[list[int]] = []
    with open(file) as f:
        for line in f:
            l = line.removesuffix("\n")
            heights.append([int(num) for num in l])
    h = Heights(heights)
    return part_a(h), part_b(h)


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    file_path = "../input.txt"
    a, b = main(file_path)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")

