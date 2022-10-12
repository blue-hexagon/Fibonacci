' Fibonacci sequence generator in QBasic
n1 = 1
n2 = 2
iter = 0
PRINT "Fibonacci Sequence Length: "
INPUT numberOfIterations
WHILE iter < numberOfIterations
  PRINT "Fib("; iter; ")="; n1
  new_number = n1 + n2
  n1 = n2
  n2 = new_number
  iter = iter+1
WEND
