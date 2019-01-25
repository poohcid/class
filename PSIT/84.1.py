"""Largest Number"""

def main(num1, num2, num3):
    """statement"""
    number = high(0, int(num1+num2+num3))
    number = high(number, int(num1+num3+num2))
    number = high(number, int(num2+num1+num3))
    number = high(number, int(num2+num3+num1))
    number = high(number, int(num3+num1+num2))
    number = high(number, int(num3+num2+num1))
    print(int(number))

def high(num1, num2):
    """high"""
    if num1 > num2:
        return num1
    else:
        return num2

main(input(), input(), input())
