class Grid:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        self.flashed: set[tuple[int, int]] = set()
        self.flash_count = 0
        self.synchronized_on_step = -1
        self.steps_taken = 0

    def get_adjacent(self, row, col) -> iter:
        for r in range(row - 1, row + 2):
            if r < 0 or r > self.row_len - 1: continue
            for c in range(col - 1, col + 2):
                if c < 0 or c > self.col_len - 1: continue
                if not (r == row and c == col):
                    yield r, c

    def inc_adjacent(self, row, col):
        for r, c in self.get_adjacent(row, col):
            if (r, c) not in self.flashed:
                self.grid[r][c] += 1
                if self.grid[r][c] > 9:
                    self.flashed.add((r, c))
                    self.inc_adjacent(r, c)

    def step(self):
        self.steps_taken += 1
        for r in range(self.row_len):
            for c in range(self.col_len):
                self.grid[r][c] += 1
                if self.grid[r][c] > 9:
                    self.flashed.add((r, c))
        for r, c in self.flashed.copy():
            self.inc_adjacent(r, c)
        for r, c in self.flashed:
            self.grid[r][c] = 0
        flashed_len = len(self.flashed)
        self.flash_count += flashed_len
        if self.synchronized_on_step == -1 and flashed_len == self.row_len * self.col_len:
            self.synchronized_on_step = self.steps_taken
        self.flashed.clear()


def part_a(grid: Grid):
    steps = 100
    for _ in range(steps):
        grid.step()
    return grid.flash_count


def part_b(grid: Grid):
    while grid.synchronized_on_step == -1:
        grid.step()
    return grid.synchronized_on_step


def main(file) -> tuple:
    grid = []
    with open(file) as f:
        for line in f:
            grid.append([int(num) for num in line if num != "\n"])
    g = Grid(grid)
    return part_a(g), part_b(g)


if __name__ == '__main__':
    import time

    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
