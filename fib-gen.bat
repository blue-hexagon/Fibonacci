REM Fibonacci sequence generator in Batch
:: Fibonacci sequence generator in Batch
@echo off & :: Inline comment
set /p numberOfIterations=Fibonacci Sequence Length: 
set n1=1
set n2=2
set iter=0

:while
if %iter% leq %numberOfIterations% (
	@echo on
	echo Fib^(%iter%^)=%n1%
	@echo off
	set /A "new_number = n1 + n2"
	set /A "n1 = n2"
	set /A "n2 = new_number"
	set /A "iter = iter + 1"
   goto :while
)
