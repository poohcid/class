"""Sequence VIII"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    for i in range(1-count, count):
        for number in range(1-count, count):
            total = count - max(abs(i), abs(number))
            print("%02d" %total, end=" ")
        print()

main()
