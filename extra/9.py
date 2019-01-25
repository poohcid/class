"""Alcoholism EP.2"""

def main():
    """main"""
    size = int(input())
    text = input()
    size2 = (size*2)+(size-1)
    print("{:^{}}" .format("*"*size, size2))
    for _ in range(size):
        print("{:^{}}" .format("*"+" "*(size-2)+"*", size2))
    space = size
    for _ in range(size-1):
        print("{:^{}}" .format("*"+" "*space+"*", size2))
        space += 2
    space -= 2
    text = ("{:.{}s}" .format(text, space))
    for i in range(size*2-1):
        if (i+1) == ((size*2-1)//2):
            if (len(text)%2 == 0 and space%2 == 0) or \
            (len(text)%2 != 0 and space%2 != 0):
                print("*{:^{}}*" .format(text, space))
            else:
                print("* {:^{}}*" .format(text, space-1))
        else:
            print("*"+" "*space+"*")
    print("*"+"*"*space+"*")


main()
