use std::io;

fn main() {
    println!("Enter an integer:");

    let mut usr_input = String::new();
    io::stdin()
        .read_line(&mut usr_input)
        .expect("Failed to read line");
    let trimmed_input = usr_input.trim();
    // parse input as i32
    let number: i32 = match trimmed_input.parse() {
        Ok(num) => num,
        Err(_) => {
            // error handling occurs here
            println!("Invalid integer");
            return;
        }
    };
    println!("Number: {}", number);
}
