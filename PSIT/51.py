"""Sequence VIII"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    space = count-1
    for i in range(1, count+1):
        print("   "*space, end="")
        for number in range(1, i+1):
            print("%02d" %number, end=" ")
        for number in range(i-1, 0, -1):
            print("%02d" %number, end=" ")
        print()
        space -= 1
    space = 1
    for i in range(count-1, 0, -1):
        print("   "*space, end="")
        for number in range(1, i+1):
            print("%02d" %number, end=" ")
        for number in range(i-1, 0, -1):
            print("%02d" %number, end=" ")
        print()
        space += 1

main()
