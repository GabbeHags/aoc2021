use std::fs;

fn get_common(arr: &[String], pos: usize) -> &str {
    let mut gamma_count = 0;
    let mut epsilon_count = 0;

    for bits in arr {
        if bits.as_bytes()[pos] == b'1' {
            gamma_count += 1;
        } else {
            epsilon_count += 1;
        }
    }

    if gamma_count >= epsilon_count {
        "1"
    } else {
        "0"
    }
}

fn flip(bit: &str) -> &str {
    if bit == "1" {
        return "0";
    }
    "1"
}

fn str_binary_to_int(bits: String) -> i32 {
    i32::from_str_radix(bits.as_str(), 2).unwrap()
}

fn part_a(v: &Vec<String>) -> i32 {
    let mut gamma = String::new();
    let mut epsilon = String::new();
    let mut common_bit: &str;
    for pos in 0..v.first().unwrap().len() {
        common_bit = get_common(&v, pos);
        gamma += common_bit;
        epsilon += flip(common_bit);
    }
    str_binary_to_int(gamma) * str_binary_to_int(epsilon)
}

fn get_rating(arr: &Vec<String>, f: bool) -> String {
    let bits_len = arr.first().unwrap().len();
    let mut result: Vec<String> = arr.clone();
    let mut common: &str;
    for i in 0..bits_len {
        let cloned_result = &result.clone(); // &result.clone();
        common = get_common(cloned_result, i);
        common = if f { flip(common) } else { common };
        result.retain(|x| x.as_bytes()[i] == common.as_bytes()[0]);
        if result.len() == 1 {
            break;
        }
    }
    result.first().unwrap().to_string()
}

fn part_b(v: &Vec<String>) -> i32 {
    let oxygen = get_rating(v, false);
    let co2 = get_rating(v, true);
    str_binary_to_int(oxygen) * str_binary_to_int(co2)
}

fn main() {
    let timer = std::time::Instant::now();
    let input_vec: Vec<String> = fs::read_to_string("../input.txt")
        .unwrap()
        .lines()
        .map(|x| x.to_string())
        .collect::<Vec<_>>();

    let a = part_a(&input_vec);
    let b = part_b(&input_vec);
    let total_time = timer.elapsed();
    println!("Result part_a: {}", a);
    println!("Result part_b: {}", b);
    println!("Time: {} sec", total_time.as_secs_f32());
}
