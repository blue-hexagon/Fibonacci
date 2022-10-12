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
