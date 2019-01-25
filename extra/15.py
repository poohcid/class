"""EZ Loop"""

def main():
    """main"""
    size = int(input())
    for i in range(1, size+1):
        for count in range(i, i+size):
            print(count, end=" ")
        print("\n", end="")
    for i in range(1, size+1):
        print(i, end=" ")
    print("\n", end="")
    for i in range(2, size+1):
        for count in range(i, size+1):
            print(count, end=" ")
        for around in range(1, i):
            print(around, end=" ")
        print("\n", end="")

main()
