"""Year"""

def main():
    """Function_input_"""
    num = int(input())
    if num <= 0:
        print("This year does not exist.")
    else:
        if (num%4) == 0 and (num%100) != 0 or (num%400) == 0:
            print("%d is leap year." %num)
        else:
            print("%d is not leap year." %num)

main()
