use std::fs;

fn is_increasing(l: Option<i32>, r: i32) -> i32 {
    if let Some(l) = l {
        if l < r {
            return 1;
        }
    }
    0
}

fn part_a(v: &[i32]) -> i32 {
    let mut prev: Option<i32> = None;
    let mut count: i32 = 0;
    for curr in v {
        count += is_increasing(prev, *curr);
        prev = Some(*curr)
    }
    count
}

fn part_b(v: &Vec<i32>) -> i32 {
    let mut prev: Option<i32> = None;
    let mut count: i32 = 0;
    let mut curr: i32;
    for i in 0..v.len() - 2 {
        curr = v[i] + v[i + 1] + v[i + 2];
        count += is_increasing(prev, curr);
        prev = Some(curr);
    }
    count
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
}
