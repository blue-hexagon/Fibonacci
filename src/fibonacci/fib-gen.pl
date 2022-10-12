$n1 = 1;
$n2 = 2;
$iter = 0;
print("Fibonacci Sequence Length: ");
$numberOfIterations = <STDIN>;
while ($iter <= $numberOfIterations){
    print("Fib($iter)=$n1\n");
    $new_number = $n1 + $n2;
    $n1 = $n2;
    $n2 = $new_number;
    $iter++;
}
