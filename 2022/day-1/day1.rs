use std::fs::File;
use std::io::prelude::*;
use std::collections::BinaryHeap;

fn main() {
    let mut file = File::open("input.txt").expect("Can't open file!");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Unable to read to line.");

    let mut calories = BinaryHeap::new();
    let mut elf_calories = 0; 

    for line in contents.lines(){ 
        if line.is_empty() { 
            calories.push(elf_calories); 
            elf_calories = 0; 
        }
        else{
            elf_calories += line.parse::<i32>().unwrap(); 
        }
    }
    

    let mut result : i32 = 0;
    let mut i = 0;  
    let num_elves = 3; 

    while i < num_elves{
        let max : i32 = calories.pop().unwrap(); 
        result += max; 
        i = i + 1; 
    }

    println!("{}", result); 
}