"""Range_Statistic"""

def main():
    """function_main"""
    high = int(input())
    if high <= 1:
        print(0)
    else:
        num1 = 0
        num2 = int(input())
        around = 1
        while around < high:
            number = int(input())
            num1 = max(num1, num2, number)
            num2 = min(num1, num2, number)
            around += 1
        print(abs(num1-num2))

main()
