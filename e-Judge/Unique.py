"""Unique"""

def main():
    """function_main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    if 1 == my_f(num1, num2, num3, num4, num5):
        final = num1
    elif 1 == my_f(num2, num3, num4, num5, num1):
        final = num2
    elif 1 == my_f(num3, num4, num5, num1, num2):
        final = num3
    elif 1 == my_f(num4, num5, num1, num2, num3):
        final = num4
    else:
        final = num5
    print(final)

def my_f(number, num2, num3, num4, num5):
    """check_function"""
    num1 = number
    score = 0
    if num1 == number:
        score += 1
    if num2 == number:
        score += 1
    if num3 == number:
        score += 1
    if num4 == number:
        score += 1
    if num5 == number:
        score += 1
    return score

main()
