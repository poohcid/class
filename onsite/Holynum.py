"""Holynum"""

def main(number, divi):
    """Function"""
    count = (number//(10**divi))
    print(count*(10**divi))

main(int(input()), int(input()))
