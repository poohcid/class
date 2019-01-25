"""Germany"""

def main():
    """function"""
    import math
    num1, num2 = int(input()), int(input())
    num3, num4 = int(input()), int(input())
    num5, num6 = int(input()), int(input())
    num7, num8 = int(input()), int(input())
    num9, num10 = int(input()), int(input())
    num1, num2 = abs(num3-num1), abs(num4-num2)
    line = math.sqrt(num1**2+num2**2)
    num1, num2 = abs(num5-num3), abs(num6-num4)
    line = line+math.sqrt(num1**2+num2**2)
    num1, num2 = abs(num7-num5), abs(num8-num6)
    line = line+math.sqrt(num1**2+num2**2)
    num1, num2 = abs(num9-num7), abs(num10-num8)
    line = line+math.sqrt(num1**2+num2**2)
    print(math.ceil(line))

main()
