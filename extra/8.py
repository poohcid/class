"""Alcoholism EP.1"""

def main():
    """main"""
    size = int(input())
    size2 = (size*2)+(size-2)
    print("{:^{}}" .format("*"*size, size2))
    for _ in range(size):
        print("{:^{}}" .format("*"+" "*(size-2)+"*", size2))
    space = size
    for _ in range(size-1):
        print("{:^{}}" .format("*"+" "*space+"*", size2))
        space += 2
    space -= 2
    for _ in range(size*2-1):
        print("*"+" "*space+"*")
    print("*"+"*"*space+"*")


main()
