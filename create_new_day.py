from pathlib import Path
import subprocess


DEFAULT_PATH: Path = Path("Solutions")
DEFAULT_DAY_NAME: str = "day"
EXAMPLE_INPUT_NAME: str = "tinput.txt"
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

def main(file) -> tuple:
    with open(file) as f:
        pass
    return part_a(), part_b()

if __name__ == '__main__':
    import time
    file_name = "../input.txt"
    start_time = time.perf_counter()
    a, b = main(file_name)
    end_time = time.perf_counter()
    print(f"Result part_a: {a}")
    print(f"Result part_b: {b}")
    print(f"Time: {(end_time - start_time):4f} sec")
    if file_name == "../tinput.txt":
        assert a == None
        assert b == None
    else:
        assert a == None
        assert b == None""")
        return True
    return False


def create_rust_file(path: Path) -> bool:
    rust_dir_path: Path = path / RUST_DIR_NAME
    if rust_dir_path.exists() is False:
        args: list[str] = ["cargo", "new", rust_dir_path]
        process_results = subprocess.run(args)
        if process_results.returncode == 0:
            rust_main_file_path = rust_dir_path / "src" / "main.rs"
            with open(rust_main_file_path, mode="w") as f:
                f.write("""use std::fs;

fn part_a(v: &[i32]) -> i32{
    -1
}

fn part_b(v: &Vec<i32>) -> i32{
    -1
}

fn main() {
    let timer = std::time::Instant::now();
    let input_vec = fs::read_to_string("../input.txt")
        .unwrap()
        .lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();
    let a = part_a(&input_vec);
    let b = part_b(&input_vec);
    let total_time = timer.elapsed();
    println!("Result part_a: {}", a);
    println!("Result part_b: {}", b);
    println!("Time: {} sec", total_time.as_secs_f32());
}""")
            return True
    return False


def main():
    day_num: str = ""

    while day_num.isnumeric() is False:
        day_num: str = input("Input the day number to create the appropriate files: ").strip()

    new_day_path: Path = DEFAULT_PATH / (DEFAULT_DAY_NAME + day_num)

    if new_day_path.exists() is False:
        new_day_path.mkdir()
        (new_day_path/EXAMPLE_INPUT_NAME).touch()

    if create_py_file(new_day_path) is False:
        print("Creating python file went wrong. exiting")
    if create_rust_file(new_day_path) is False:
        print("Creating rust files went wrong. exiting")

    print("Done")


if __name__ == '__main__':
    main()