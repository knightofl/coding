extern crate rand;

use std::io;
use rand::Rng;

fn main() {
    println!("숫자 맞추기!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("추측한 숫자는?");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
               .expect("읽기 실패!");

    println!("당신이 생각한 숫자는 : {}", guess);
    println!("비밀의 번호는 : {}", secret_number);
}
