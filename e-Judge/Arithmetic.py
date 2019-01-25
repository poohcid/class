"""Arithmetic"""

def main():
    """function_main"""
    num1 = int(input())
    many = int(input())
    diff = int(input())
    total = ""
    for _ in range(many):
        total = total+str(num1)+" "
        num1 += diff
    print(total)

main()
