var n1: number = 1;
var n2: number = 2;
var iter: number = 0;
var numberOfIterations: number = prompt("Fibonacci Sequence Length ") as any;
while (iter <= numberOfIterations){
    console.log(`Fib(${iter})=${n1}`);
    var new_number: number = n1 + n2;
    n1 = n2;
    n2 = new_number;
    iter++;
}