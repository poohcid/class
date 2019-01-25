"""FibonacciRecursionV1"""

def main(count, num1, num2):
    """FibonacciRecursionV1"""
    if count == 0:
        print(num2)
    else:
        main(count-1, num2, num1+num2)

main(int(input()), 1, 0)
