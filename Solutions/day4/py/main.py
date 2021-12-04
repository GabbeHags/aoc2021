def has_bingo(board) -> bool:
    for row in board:
        if all((mark for _, mark in row)):
            return True
    for row in zip(*board):
        if all((mark for _, mark in row)):
            return True
    return False


def mark_nums(num, board):
    board_len = len(board)
    for row in range(board_len):
        for col in range(board_len):
            _num, marked = board[row][col]
            if _num == num:
                board[row][col] = (_num, True)


def sum_unmarked(board) -> int:
    total = 0
    for row in board:
        total += sum([num for num, mark in row if not mark])
    return total


def part_a(nums: list[int], boards: list[list[list[tuple[int, bool]]]]) -> int:
    for num in nums:
        for board in boards:
            mark_nums(num, board)  # inplace
            if has_bingo(board):
                return sum_unmarked(board) * num


def part_b(nums: list[int], boards: list[list[list[tuple[int, bool]]]]) -> int:
    boards_with_bingo = []
    for num in nums:
        for board in boards:
            if not has_bingo(board):
                mark_nums(num, board)  # inplace
                if has_bingo(board):
                    boards_with_bingo.append((board, num))
    last_board_to_get_bingo, num = boards_with_bingo.pop()
    return sum_unmarked(last_board_to_get_bingo) * num


def load_bingo_board(input_str):
    matrix: list[list[tuple[int, bool]]] = []
    for line in input_str:
        if line == "\n":
            break
        matrix.append([(int(num), False) for num in line.split(" ") if num != ""])
    return matrix


def reset_boards(boards):
    for board in boards:
        for row in range(len(board)):
            for col in range(len(board[row])):
                num, _ = board[row][col]
                board[row][col] = (num, False)
    return boards


def main() -> tuple:
    bingo_nums: list[int]
    bingo_boards: list[list[list[tuple[int, bool]]]] = []

    with open("../input.txt") as f:
        bingo_nums = [int(num) for num in f.readline().split(",")]
        f.readline()
        while True:
            matrix = load_bingo_board(f)
            if len(matrix) == 0:
                break
            bingo_boards.append(matrix)

    return part_a(bingo_nums, bingo_boards), part_b(bingo_nums, reset_boards(bingo_boards))


if __name__ == '__main__':
    import time

    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
