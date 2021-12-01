from pathlib import Path
import subprocess


DEFAULT_PATH: Path = Path("Solutions")
DEFAULT_DAY_NAME: str = "day"
PY_DIR_NAME: str = "py"
PY_FILE_NAME: str = "main.py"
RUST_DIR_NAME: str = "rust"


def create_py_file(path: Path) -> bool:
    py_dir_path: Path = path / PY_DIR_NAME
    py_file_path: Path = py_dir_path / PY_FILE_NAME
    if py_dir_path.exists() is False:
        py_dir_path.mkdir()
        with open(py_file_path, mode="w") as f:
            f.write("""def part_a():
    pass

def part_b():
    pass

def main() -> tuple:
    with open("../input.txt") as f:
        pass
    return part_a(), part_b()

if __name__ == '__main__':
    import time
    start_time = time.perf_counter()
    a, b = main()
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")""")
        return True
    return False


def create_rust_file(path: Path) -> bool:
    rust_dir_path: Path = path / RUST_DIR_NAME
    if rust_dir_path.exists() is False:
        args: list[str] = ["cargo", "new", rust_dir_path]
        process_results = subprocess.run(args)
        if process_results.returncode == 0:
            return True
    return False


def main():
    day_num: str = ""

    while day_num.isnumeric() is False:
        day_num: str = input("Input the day number to create the appropriate files: ").strip()

    new_day_path: Path = DEFAULT_PATH / (DEFAULT_DAY_NAME + day_num)

    if new_day_path.exists() is False:
        new_day_path.mkdir()

    if create_py_file(new_day_path) is False:
        print("Creating python file went wrong. exiting")
        exit(-1)
    if create_rust_file(new_day_path) is False:
        print("Creating rust files went wrong. exiting")
        exit(-1)

    print("Everything went fine. :)")


if __name__ == '__main__':
    main()
