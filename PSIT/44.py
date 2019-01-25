"""Sequence V"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    add = 1
    for i in range(count, 0, -1):
        if add == 7:
            print()
            add = 1
        print(i, end=" ")
        add += 1

main()
