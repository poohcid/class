"""Year"""

def main():
    """Function_input_"""
    number = int(input())
    if (number%4) == 0:
        if (number%100) == 0:
            if (number%400) == 0:
                print("%d is leap year." %number)
            else:
                print("%d is not leap year." %number)
        else:
            print("%d is leap year." %number)
    else:
        if (number < 0):
            print("This year does not exist.")
        else:
            print("%d is not leap year." %number)

main()
