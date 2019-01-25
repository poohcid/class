"""Nearer"""

def main():
    """Nearer"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if abs(num3-num1) < abs(num3-num2):
        print("Alice %d" %abs(num3-num1))
    elif abs(num3-num2) < abs(num3-num1):
        print("Bob %d" %abs(num3-num2))
    else:
        print("Sundaes %d" %abs(num3-num2))

main()
