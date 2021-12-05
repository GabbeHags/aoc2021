class LineSegment:

    def __init__(self, line_segment_str: str):
        (self.x1, self.y1), (self.x2, self.y2) = map(lambda x: map(lambda y: int(y), x.split(",")),
                                                     line_segment_str.split(" -> "))

    def is_straight(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def covers(self) -> list[tuple[int, int]]:
        result = []
        if self.x1 == self.x2:
            result.extend(self._covers_straight_in_y())
        elif self.y1 == self.y2:
            result.extend(self._covers_straight_in_x())
        else:
            result.extend(self._covers_diagonal())
        return result

    def _covers_diagonal(self) -> list[tuple[int, int]]:
        x_diff = self.x2 - self.x1
        y_diff = self.y2 - self.y1
        diff = abs(x_diff)
        result = [None]*(diff+1)
        index = 0
        if x_diff == y_diff:
            if x_diff > 0:
                #  * x_diff == y_diff and diff > 0 -> inc both of the sides and add each step to the result until x1 == x2 and y1 == y2
                for n in range(diff + 1):
                    result[index] = (self.x1 + n, self.y1 + n)
                    index += 1
            else:
                #  * x_diff == y_diff and diff < 0 -> dec both of the sides and add each step to the result until x1 == x2 and y1 == y2
                for n in range(diff + 1):
                    n = -1 * n
                    result[index] = (self.x1 + n, self.y1 + n)
                    index += 1

        elif x_diff > y_diff:
            #  * x_diff >  y_diff -> inc x1 and dec y1 until x1 == x2 and y1 == y2
            for n in range(diff + 1):
                result[index] = (self.x1 + n, self.y1 + (-1 * n))
                index += 1

        elif x_diff < y_diff:
            #  * x_diff <  y_diff -> dec x1 and inc y1 until x1 == x2 and y1 == y2
            for n in range(diff + 1):
                result[index] = (self.x1 + (-1 * n), self.y1 + n)
                index += 1
        return result

    def _covers_straight_in_y(self) -> list[tuple[int, int]]:
        result = [None]*(abs(self.y2 - self.y1) + 1)
        index = 0
        if self.y2 > self.y1:
            for n in range(self.y1, self.y2 + 1):
                result[index] = (self.x1, n)
                index += 1
        else:
            for n in range(self.y1, self.y2 - 1, -1):
                result[index] = (self.x1, n)
                index += 1
        return result

    def _covers_straight_in_x(self) -> list[tuple[int, int]]:
        result = [None]*(abs(self.x2 - self.x1) + 1)
        index = 0
        if self.x2 > self.x1:
            for n in range(self.x1, self.x2 + 1):
                result[index] = (n, self.y1)
                index += 1
        else:
            for n in range(self.x1, self.x2 - 1, -1):
                result[index] = (n, self.y1)
                index += 1
        return result


def part_a(line_segments) -> int:
    coords = {}
    for segment in line_segments:
        if segment.is_straight():
            for coord in segment.covers():
                if coord in coords:
                    coords[coord] += 1
                else:
                    coords[coord] = 1
    return sum(map(lambda x: x > 1, coords.values()))


def part_b(line_segments):
    coords = {}
    for segment in line_segments:
        for coord in segment.covers():
            if coord in coords:
                coords[coord] += 1
            else:
                coords[coord] = 1
    return sum(map(lambda x: x > 1, coords.values()))


def main() -> tuple:
    line_segments = []
    with open("../input.txt") as f:
        for line in f:
            line_segments.append(LineSegment(line))
    return part_a(line_segments), part_b(line_segments)


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
