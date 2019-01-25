"""Sequence I"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    for _ in range(count):
        for i in range(1, count+1):
            print(i, end=" ")
        print()

main()
