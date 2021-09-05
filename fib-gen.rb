if __FILE__ == $0
  n1=1
  n2=2
  iter=0
  puts "Fibonacci Sequence Length: "
  numberOfIterations = gets.to_i

  while iter <= numberOfIterations do
    puts "Fib(#{iter})=#{n1}"  
    new_number = n1 + n2
    n1 = n2
    n2 = new_number
    iter+=1
  end
end