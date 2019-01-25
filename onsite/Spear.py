"""Spear"""

def main(size):
    """Function_input_"""
    space1, space2 = size//2, -1
    print(" "*space1+"*")
    space1 -= 1
    space2 += 1
    for count in range(size-2):
        if count < ((size-2)//2):
            print(" "*space1+"* "+"  "*space2+"*")
            space1 -= 1
            space2 += 1
        else:
            print(" "*space1+"* "+"  "*space2+"*")
            space1 += 1
            space2 -= 1
    if size > 1:
        print(" "*space1+"*")
    for _ in range(size):
        print(" "*space1+"*")

main(int(input()))
