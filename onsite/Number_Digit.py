"""Number_Digit"""

def main():
    """main"""
    number = str(abs(int(input())))
    number = number[::-1]
    digit = int(input())
    if digit <= 0:
        print("Index error.")
    elif digit <= len(number):
        print(number[digit-1:digit])
    else:
        print("Index out of range.")

main()
