place_holder_empty = "."
place_holder_mark = "#"
place_holder_fold_x = "@"
place_holder_fold_y = "@"


def fold(grid, x=None, y=None):
    assert x is not None or y is not None
    if x:
        tmp_grid = []
        new_grid = []
        for row in grid:
            assert place_holder_mark != row[x], f"x = {x}, {row[x]}"
            # row[x] = place_holder_fold_x
            tmp_grid.append([row[n] for n in range(x+1, len(row))])
            new_grid.append([row[n] for n in range(x)])
        return merge_folds(new_grid, [list(reversed(x)) for x in tmp_grid])

    else:
        # assert place_holder_mark not in grid[y], f"y = {y}, \"{place_holder_mark}\" found at index: {grid[y].index(place_holder_mark)} \n{grid[y]}"
        # grid[y] = [place_holder_fold_y] * len(grid[y])
        tmp_grid = [list(row) for row in zip(*zip(*[grid[row] for row in range(y + 1, len(grid))][::-1]))]
        new_grid = [grid[row] for row in range(y)]
        return merge_folds(new_grid, tmp_grid)


def merge_folds(g1, g2):
    g1_h = len(g1)
    g2_h = len(g2)
    g1_w = len(g1[0])
    g2_w = len(g2[0])
    if g1_h > g2_h:
        h = g2_h
    else:
        h = g1_h
    if g1_w > g2_w:
        w = g2_w
    else:
        w = g1_w
    g = [[place_holder_empty for _ in range(w)] for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if r < g2_h and c < g2_w:
                g2_dot = g2[r][c]
            else:
                g2_dot = place_holder_empty
            if r < g1_h and c < g1_w:
                g1_dot = g1[r][c]
            else:
                g1_dot = place_holder_empty
            if g1_dot == place_holder_mark or g2_dot == place_holder_mark:
                g[r][c] = place_holder_mark
    return g


def count_marked(grid):
    count = 0
    for row in grid:
        for dot in row:
            if dot == place_holder_mark:
                count += 1
    return count


def part_a(dots, folds):
    max_x = max((x for x, _ in dots)) + 1
    max_y = max((y for _, y in dots)) + 1
    grid = [[place_holder_empty for _ in range(max_x)] for _ in range(max_y)]
    for dot in dots:
        x, y = dot
        grid[y][x] = place_holder_mark
    for direction, at in folds:
        if direction == "x":
            grid = fold(grid, x=at)
        if direction == "y":
            grid = fold(grid, y=at)
        break

    return count_marked(grid)


def part_b(dots, folds):
    max_x = max((x for x, _ in dots)) + 1
    max_y = max((y for _, y in dots)) + 1
    grid = [[place_holder_empty for _ in range(max_x)] for _ in range(max_y)]
    for dot in dots:
        x, y = dot
        grid[y][x] = place_holder_mark
    for direction, at in folds:
        if direction == "x":
            print("x: ", at)
            grid = fold(grid, x=at)
        if direction == "y":
            print("y: ", at)
            grid = fold(grid, y=at)

    for row in grid:
        print(row)
    return count_marked(grid)


def main(file) -> tuple:
    with open(file) as f:
        _dots, _folds = f.read().split("\n\n")
        dots = [tuple(int(n) for n in dot.split(",")) for dot in _dots.split("\n")]
        folds = []
        for _fold in _folds.strip().split("\n"):
            direction, at = _fold.removeprefix("fold along ").split("=")
            folds.append((direction, int(at)))
    return part_a(dots, folds), part_b(dots, folds)


if __name__ == '__main__':
    import time

    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
