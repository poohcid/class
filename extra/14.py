"""Diffy Game"""

def main():
    """main"""
    num1, num2 = int(input()), int(input())
    num3, num4 = int(input()), int(input())
    print("%d\t%d\t%d\t%d" %(num1, num2, num3, num4))
    score = 0
    while (num1 != 0) or (num2 != 0) or (num3 != 0) or (num4 != 0):
        score += 1
        num1, num2, num3, num4 = abs(num1-num2), abs(num2-num3),\
        abs(num3-num4), abs(num4-num1)
        print("%d\t%d\t%d\t%d" %(num1, num2, num3, num4))
    print(score)

main()
