"""Count Type"""

def main():
    """main"""
    text = input()
    upper, lower, number, other = 0, 0, 0, 0
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isnumeric():
            number += 1
        else:
            other += 1
    print("Uppercase : %d" %upper)
    print("Lowercase : %d" %lower)
    print("Numeric : %d" %number)
    print("Other : %d" %other)

main()
