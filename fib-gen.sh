read -p "Fibonacci Sequence Length:" numberOfIterations 
n1=1
n2=2
iter=0
while [[ ${iter} -le ${numberOfIterations} ]]
do
echo "Fib(${iter})=${n1}"
((iter++))
((new_number=n1+n2))
((n1=n2))
((n2=new_number))
done
