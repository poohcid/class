"""Diginity_Midterm2014"""

def main(number, final):
    """total to 1-9"""
    while int(number) != 0:
        total = sum([int(i) for i in str(number)])
        while total >= 10:
            total = sum([int(i) for i in str(total)])
        final += str(total)+"\n"
        number = input()
    return final

print(main(int(input()), ""))
