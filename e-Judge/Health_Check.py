"""Health_Check"""

def main():
    """function"""
    cm1 = float(input())
    cm2 = float(input())
    cm3 = float(input())
    cm4 = float(input())
    cm5 = float(input())
    average = (cm1+cm2+cm3+cm4+cm5)/5
    num1 = max(cm1, cm2)
    num2 = max(cm3, cm4)
    num3 = max(num1, num2)
    tall = max(num3, cm5)
    num1 = min(cm1, cm2)
    num2 = min(cm3, cm4)
    num3 = min(num1, num2)
    low = min(num3, cm5)
    print("The Tallest is %.1f" %tall)
    print("The Shortest is %.1f" %low)
    print("Average is %.1f" %average)

main()
