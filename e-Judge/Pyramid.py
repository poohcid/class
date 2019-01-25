"""Pyramid"""

def main():
    """function_main"""
    high = int(input())
    space = high-1
    star = 1
    for _ in range(high):
        print(" "*space+"*"*star, end="\n")
        space -= 1
        star += 2

main()
