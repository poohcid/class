"""Pyramid"""

def main(high):
    """Function_input_"""
    space, star = high-1, 1
    for _ in range(high):
        print(" "*space+"*"*star)
        space -= 1
        star += 2

main(int(input()))
