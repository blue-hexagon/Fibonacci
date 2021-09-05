$numberOfIterations = Read-Host "Fibonacci Sequence Length: "
$n1=1
$n2=2
$iter=0

DO {
    Write-Host "Fib(${iter})=${n1}"
	$new_number = $n1 + $n2
	$n1 = $n2
	$n2 = $new_number
	$iter = $iter+1
} While ($iter -le $numberOfIterations)


