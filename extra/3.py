"""ThreeSUM"""

def main(number):
    """Function_input_"""
    add2 = prison(number, number, "|", 0)
    add2 = prison(number, 1, "#", add2)
    prison(number, number, "|", add2)

def prison(number1, number2, text, add2):
    """print_prison_half"""
    for _ in range(number2):
        for _ in range(number1):
            if add2 == 0:
                print("+", end="")
                add2 = 1
            else:
                print("-", end="")
                add2 = 0
        print("%s" %text, end="")
        for _ in range(number1):
            if add2 == 1:
                print("+", end="")
                add2 = 0
            else:
                print("-", end="")
                add2 = 1
        if add2 == 0:
            add2 = 1
        else:
            add2 = 0
        print("\n", end="")
    return add2

main(int(input())//2)
