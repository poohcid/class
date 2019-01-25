"""Doubling"""

def main():
    """function_main"""
    power = int(input())
    num1 = 2
    for num2 in range(0, power+1):
        print(num1**num2)
        num2 += 1

main()
