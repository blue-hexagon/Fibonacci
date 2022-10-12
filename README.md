
# What is This?
The objective of this repository is to write a fibonacci sequence generator in many languages.

# Completed
            
## [Basic](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.bas)

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


## [Batch](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.bat)

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


## [C#](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.cs)

	using System;
	
	class MainClass {
	  public static void Main (string[] args) {
	    short iter = 0, numberOfIterations;
	    int n1 = 1, n2 = 2;
	    Console.WriteLine("Fibonacci Sequence Length: ");
	    numberOfIterations = Convert.ToInt16(Console.ReadLine());
	    while (iter <= numberOfIterations){
	      Console.WriteLine($"Fib({iter})={n1}");
	      int new_number = (n1 + n2);
	      n1 = n2;
	      n2 = new_number;
	      iter++;
	    }
	  }
	}


## [Go](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.go)

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


## [Java](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.java)

	import java.util.Scanner;
	
	class Main {
	  public static void main(String[] args) {
	  Scanner scanner = new Scanner(System.in);
	  System.out.println("Fibonacci Sequence Length: ");
	  int numberOfIterations = Integer.parseInt(scanner.nextLine());
	  int n1 = 1;
	  int n2 = 2;
	  int iterator = 0;
	  while (iterator <= numberOfIterations){
	    System.out.println("Fib(" + iterator + ")=" + n1);
	    int new_number = n1 + n2;
	    n1 = n2;
	    n2 = new_number;
	    iterator++;
	    }
	  }
	}


## [JavaScript](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.js)

	// Fibonacci sequence generator in Javascript
	
	/*
	Fibonacci sequence generator in Javascript
	*/
	
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


## [Lua](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.lua)

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


## [Perl](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.pl)

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


## [Powershell](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.ps1)

	# Fibonacci sequence generator in Powershell
	
	<#
	Fibonacci sequence generator in Powershell
	#>
	
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


## [Python](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.py)

	if __name__ == "__main__":
	    numberOfIterations = input("Fibonacci Sequence Length: ")
	    n1 = 1
	    n2 = 2
	    iterator = 0
	    while iterator <= int(numberOfIterations):
	        print(f"Fib({iterator})={n1}")
	        new_number = n1 + n2
	        n1 = n2
	        n2 = new_number
	        iterator += 1


## [Ruby](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.rb)

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


## [Rust](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.rs)

	// Fibonacci sequence generator in Rust
	/* Fibonacci sequence generator in Rust */
	fn main() {
	    let mut n1: i16 = 1;
	    let mut n2: i16 = 2;
	    let mut iter: i16 = 0;
	    let number_of_iterations: i16 = 10;
	
	      while iter <= number_of_iterations {
	        println!("Fib({})={}",iter,n1);
	        let new_number: i16 = n1 + n2;
	        n1 = n2;
	        n2 = new_number;
	        iter += 1;
	      }
	  }


## [Bash](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.sh)

	# Fibonacci sequence generator in Bash
	
	<< 'COMMENT'
	  A non redirected heredoc can serve as a multiline comment.
	  This is a hack though.
	COMMENT
	
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


## [TypeScript](https://github.com/blue-hexagon/Fibonacci-In-Many-Languages/blob/master/src/fibonacci/fib-gen.ts)

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

