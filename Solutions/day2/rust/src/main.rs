use std::fs;


struct Command {
    cmd: Cmds,
    num: i32
}

enum Cmds {
    Forward,
    Up,
    Down
}

impl Command {

    fn parse(s: &str) -> Command{
        const COMMAND_FORWARD: &str = "forward";
        const COMMAND_UP: &str = "up";
        const COMMAND_DOWN: &str = "down";

        let (cmd, num) = s.split_once(" ").unwrap();
        let cmd = match cmd {
            COMMAND_FORWARD => Cmds::Forward,
            COMMAND_UP      => Cmds::Up,
            COMMAND_DOWN    => Cmds::Down,
            _               => panic!()
        };
        Command {
            cmd,
            num: num.parse().unwrap()
        }
    }
}

fn part_a(v: &[Command]) -> i32{
    let mut horizontal = 0;
    let mut depth = 0;
    for command in v {
        match command.cmd {
            Cmds::Forward => horizontal += command.num,
            Cmds::Up      => depth -= command.num,
            Cmds::Down    => depth += command.num,
        };
    }
    horizontal * depth
}

fn part_b(v: &[Command]) -> i32{
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for command in v {
        match command.cmd {
            Cmds::Forward => {
                horizontal += command.num;
                depth += aim*command.num;
            },
            Cmds::Up      => aim -= command.num,
            Cmds::Down    => aim += command.num,
        };
    }
    horizontal * depth
}

fn main() {
    let timer = std::time::Instant::now();
    let input_vec = fs::read_to_string("../input.txt")
        .unwrap()
        .lines()
        .map(|x| Command::parse(x))
        .collect::<Vec<_>>();
    let a = part_a(&input_vec);
    let b = part_b(&input_vec);
    let total_time = timer.elapsed();

    println!("Result part_a: {}", a);
    println!("Result part_b: {}", b);
    println!("Time: {} sec", total_time.as_secs_f32());
}