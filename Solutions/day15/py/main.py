from collections import defaultdict, Counter
import heapq


class Graph:

    def __init__(self, grid):
        self.grid = grid
        self.grid_rows = len(grid)
        self.grid_cols = len(grid[0])
        self.visited = set()
        self.edges = defaultdict(Counter)
        self._gen_edges()

    def adjacent(self, row, col) -> iter:
        if row < self.grid_rows - 1:
            yield row + 1, col
        if row > 0:
            yield row - 1, col
        if col < self.grid_cols - 1:
            yield row, col + 1
        if col > 0:
            yield row, col - 1

    def _add_edge(self, _from, to):
        self.edges[_from][to] = self.grid[to[0]][to[1]]

    def _gen_edges(self):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                curr = (r, c)
                for adj in self.adjacent(r, c):
                    self._add_edge(curr, adj)

    def dijkstra(self, start):
        costs = {p: float('inf') for p in self.edges}
        costs[start] = 0
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            _, curr = heapq.heappop(pq)
            self.visited.add(curr)

            for neighbor in self.edges[curr]:
                dist = self.edges[curr][neighbor]
                if neighbor not in self.visited:
                    old_cost = costs[neighbor]
                    new_cost = costs[curr] + dist
                    if new_cost < old_cost:
                        heapq.heappush(pq, (new_cost, neighbor))
                        costs[neighbor] = new_cost
        return costs


def inc(grid, row_len, col_len):
    new_grid = [[None for _ in range(col_len)] for _ in range(row_len)]
    for r in range(row_len):
        for c in range(col_len):
            new_grid[r][c] = 1 + grid[r][c] if grid[r][c] != 9 else 1
    return new_grid


def part_a(grid):
    g = Graph(grid)
    start_pos = (0, 0)
    end_pos = (g.grid_rows - 1, g.grid_cols - 1)

    return g.dijkstra(start_pos)[end_pos]

# from misc.misc_funcs import profile_func
# @profile_func
def part_b(grid):
    grid_container: list[list] = []
    size = 5
    row_len = len(grid)
    cols_len = len(grid[0])

    for _ in range(size):
        rows = [grid]
        for _ in range(size-1):
            grid = inc(grid, row_len, cols_len)
            rows.append(grid)
        grid_container.append(rows)
        grid = rows[1]

    giga_grid = [[None for _ in range(cols_len*5)] for _ in range(row_len*5)]
    for r in range(size):
        for c in range(size):
            for rr in range(row_len):
                for cc in range(cols_len):
                    row = rr + r*row_len
                    col = cc + c*cols_len
                    giga_grid[row][col] = grid_container[r][c][rr][cc]

    g = Graph(giga_grid)
    start_pos = (0, 0)
    end_pos = (g.grid_rows - 1, g.grid_cols - 1)

    return g.dijkstra(start_pos)[end_pos]


def main(file) -> tuple:
    with open(file) as f:
        grid = [[int(num) for num in line.strip()] for line in f]
    return part_a(grid), part_b(grid)


if __name__ == '__main__':
    import time

    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
