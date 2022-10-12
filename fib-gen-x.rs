// Fibonacci sequence generator in Rust
/* Fibonacci sequence generator in Rust */
fn main() {
    let mut n1: i16 = 1;
    let mut n2: i16 = 2;
    let mut iter: i16 = 0;
    let number_of_iterations: i16 = 10;
    
      while iter <= number_of_iterations {
        println!("Fib({})={}",iter,n1);
        let new_number: i16 = n1 + n2;
        n1 = n2;
        n2 = new_number;
        iter += 1;
      }
  }
  
