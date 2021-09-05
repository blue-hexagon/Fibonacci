package main

import "fmt"

func main() {
  fmt.Println("Fibonacci Sequence Length: ")
  var numberOfIterations int
  fmt.Scanf("%v", &numberOfIterations)
  var n1, n2 int = 1, 2
  iter := 0
  for iter <= numberOfIterations {
    fmt.Printf("Fib(%v)=%v\n",iter,n1)
    new_number := n1 + n2
    n1 = n2
    n2 = new_number
    iter++
  }
}