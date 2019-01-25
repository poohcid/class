"""Geometric"""

def main():
    """function_main"""
    num1 = float(input())
    many = int(input())
    ratio = float(input())
    total = ""
    for _ in range(many):
        total = ("%s%.2f " %(total, num1))
        num1 *= ratio
    print(total)

main()
