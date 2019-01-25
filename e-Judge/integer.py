"""Digits"""

def main():
    """function_input_"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num1 = (num1%10)
    num2 = ((num2%100)//10)
    num3 = ((num3%1000)//100)
    num4 = ((num4%10000)//1000)
    num5 = (num5//100000)
    total = num5+num4+num2+num3+num1
    print("%d+%d+%d+%d+%d = %d" %(num1, num2, num3, num4, num5, total))
main()
