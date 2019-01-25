"""Sort"""

def main():
    """function"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num1, num2 = max(num1, num2), min(num1, num2)
    num3, num4 = max(num3, num4), min(num3, num4)
    num1, num3 = max(num1, num3), min(num1, num3)
    num1, num4 = max(num1, num4), min(num1, num4)
    num2, num3 = max(num2, num3), min(num2, num3)
    num2, num4 = max(num2, num4), min(num2, num4)
    num3, num4 = max(num3, num4), min(num3, num4)
    print("%d\n%d\n%d\n%d" %(num1, num2, num3, num4))

main()
