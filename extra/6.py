"""Print i"""

def main():
    """main"""
    style = input()
    num1, num2, num3 = int(input()), int(input()), 1
    if num2 < num1:
        num3, num2 = -1, num2-2
    for i in range(num1, num2+1, num3):
        if style == "Vertical":
            print("%02d" %i)
        elif style == "Horizontal":
            print("%02d" %i, end=" ")

main()
