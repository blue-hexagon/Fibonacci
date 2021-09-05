local n1 = 1
local n2 = 2
local iter = 0
print('Fibonacci Sequence Length: ')
local numberOfIterations = io.read("*n")

while iter <= numberOfIterations do
  print("Fib(".. iter .. ")=" .. n1)
  -- the-strf-way: print(string.format("Fib(%s)=%d",iter,n1))
  new_number = n1 + n2
  n1 = n2
  n2 = new_number
  iter = iter + 1
end