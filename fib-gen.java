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