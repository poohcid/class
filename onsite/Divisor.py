"""Cake"""

def main():
    """Function_input_"""
    num1, num2 = int(input()), int(input())
    num1, num2 = min(num1, num2), max(num1, num2)
    divi = num1
    while divi > 1:
        if (num1%divi == 0) and (num2%divi == 0):
            break
        else:
            divi -= 1
    print(divi)

main()
