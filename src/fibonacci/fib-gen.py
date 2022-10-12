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
