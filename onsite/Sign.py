"""Sign"""

def main():
    """main"""
    size = int(input())
    text = input()
    sign = input()
    text = ("{:.{}s}" .format(text, size-2))
    print("*"*size)
    print("*"+" "*(size-2)+"*")
    if sign == "Left":
        print("*{:<{}}*" .format(text, size-2))
    elif sign == "Right":
        print("*{:>{}}*" .format(text, size-2))
    elif sign == "Center":
        if len(text)%2 == 0:
            print("*{:^{}}*" .format(text, size-2))
        else:
            print("* {:^{}}*" .format(text, size-3))
    print("*"+" "*(size-2)+"*")
    print("*"*size)

main()
