let n1 = 1
let n2 = 2
let iter = 0
const numberOfIterations = prompt("Fibonacci Sequence Length ");

while (iter <= numberOfIterations){
  console.info(`Fib(${iter})=${n1}`)
  new_number = n1 + n2
  n1 = n2
  n2 = new_number
  iter++
}