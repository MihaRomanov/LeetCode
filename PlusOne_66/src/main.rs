fn increment_large_integer(digits: &mut Vec<i32>) -> Vec<i32> {
    // Convert the digits array into an integer
    let mut num = 0;
    for &digit in digits.iter() {
        num = num * 10 + digit;
    }

    // Increment the integer by one
    num += 1;

    // Convert the updated integer back into an array of digits
    let mut result = Vec::new();
    while num > 0 {
        result.push(num % 10);
        num /= 10;
    }
    result.reverse();

    result
}

fn main() {
    let mut digits1 = vec![1, 2, 3];
    let mut digits2 = vec![4, 3, 2, 1];
    let mut digits3 = vec![9];

    let result1 = increment_large_integer(&mut digits1);
    let result2 = increment_large_integer(&mut digits2);
    let result3 = increment_large_integer(&mut digits3);

    println!("Result 1: {:?}", result1); // [1, 2, 4]
    println!("Result 2: {:?}", result2); // [4, 3, 2, 2]
    println!("Result 3: {:?}", result3); // [1, 0]
}