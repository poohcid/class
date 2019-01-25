"""Calculus"""

def main():
    """function"""
    num1 = float(input())
    num2 = float(input())
    num2, num1 = max(num1, num2), min(num1, num2)
    area = ((num2**3)/3+num2)-((num1**3)/3+num1)
    print("%.2f" %area)

main()
