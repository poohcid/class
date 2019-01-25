"""Number_Game"""

def main():
    """Function_input_"""
    number = int(input())
    snum1 = int(input())
    gnum1 = int(input())
    snum2 = int(input())
    gnum2 = int(input())
    snum3 = int(input())
    gnum3 = int(input())
    snum = abs(number-(snum1+snum2+snum3))
    gnum = abs(number-(gnum1+gnum2+gnum3))
    if snum < gnum:
        print("Saint won!")
    elif gnum < snum:
        print("Gunn won!")
    else:
        print("Draw!")

main()
