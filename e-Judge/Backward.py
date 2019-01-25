"""Backward"""

def main():
    """function_main"""
    num1 = int(input())
    num2 = int(input())
    for number in range(num1, -1, -num2):
        print(number)

main()
