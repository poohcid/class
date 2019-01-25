"""Clock"""

def main(size):
    """Function_input_"""
    space1, space2 = size//2, -1
    print(" "*space1+"*")
    for _ in range(size//2):
        print(" "*space1+"* "+"  "*space2+"*")
        space1 -= 1
        space2 += 1
    space1 = 1
    space2 -= 2
    for _ in range(size//2-1):
        print(" "*space1+"* "+"  "*space2+"*")
        space1 += 1
        space2 += 1

main(int(input()))
