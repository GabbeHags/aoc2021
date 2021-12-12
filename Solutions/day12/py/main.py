from collections import deque


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.connected_to: set[Cave] = set()
        self.visited = False

    def find_all_paths_part_a(self, to, path=None):
        if path is None:
            path = deque()
        count = 0
        self.visit()
        path.append(self.name)
        for cave in self.connected_to:
            if cave.name == to:
                count += 1
            else:
                if cave.can_visit():
                    count += cave.find_all_paths_part_a(to, path)
        self.un_visit()
        path.pop()
        return count

    def find_all_paths_part_b(self, to, path=None, all_paths=None):
        if all_paths is None:
            all_paths = set()
        if path is None:
            path = deque()
        self.visit()
        path.append(self.name)
        for cave in self.connected_to:
            if cave.name == to:
                all_paths.add(str(path))
            else:
                if cave.can_visit():
                    ap = cave.find_all_paths_part_b(to, path, all_paths)
                    for _cave in ap:
                        all_paths.add(_cave)
        self.un_visit()
        path.pop()
        return all_paths

    def can_visit(self):
        return True

    def visit(self):
        self.visited = True

    def un_visit(self):
        self.visited = False

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()


class SmallCave(Cave):
    def __init__(self, name: str):
        super().__init__(name)
        self.visit_tickets = 1

    def visit(self):
        super().visit()
        self.visit_tickets -= 1

    def un_visit(self):
        super().un_visit()
        self.visit_tickets += 1

    def can_visit(self):
        return self.visit_tickets > 0


def part_a(start_cave: Cave):
    return start_cave.find_all_paths_part_a("end")


def part_b(start_cave: Cave, caves):
    all_paths = set()
    for cave in caves.values():
        if cave.name != "start" and cave.name != "end":
            print(f"on cave: {cave.name}")
            cave.un_visit()
            paths = start_cave.find_all_paths_part_b("end")
            cave.visit()
            for _cave in paths:
                all_paths.add(_cave)
    return len(all_paths)


def make_cave(name: str) -> Cave:
    if name.isupper():
        return Cave(name)
    else:
        return SmallCave(name)


def main(file) -> tuple:
    caves: dict[str, Cave] = dict()
    with open(file) as f:
        for line in f:
            left, right = line[:-1].split("-")
            if left in caves and right in caves:
                caves[left].connected_to.add(caves[right])
                caves[right].connected_to.add(caves[left])
            elif left in caves:
                right_cave = make_cave(right)
                caves[left].connected_to.add(right_cave)
                caves[right] = right_cave
                caves[right].connected_to.add(caves[left])
            elif right in caves:
                left_cave = make_cave(left)
                caves[right].connected_to.add(left_cave)
                caves[left] = left_cave
                caves[left].connected_to.add(caves[right])
            else:
                left_cave = make_cave(left)
                right_cave = make_cave(right)
                left_cave.connected_to.add(right_cave)
                right_cave.connected_to.add(left_cave)
                caves[left] = left_cave
                caves[right] = right_cave

    return part_a(caves["start"]), part_b(caves["start"], caves)


if __name__ == '__main__':
    import time
    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
