"""Perfectionist"""

def main(number):
    """Function"""
    if number <= 0:
        print("Not Perfect")
    elif (number > 100) and (number%10 == 0 or number%25 == 0):
        print("Perfect")
    elif (number <= 100) and (number%5 == 0):
        print("Perfect")
    else:
        print("Not Perfect")

main(int(input()))
