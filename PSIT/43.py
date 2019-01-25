"""Sequence III"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    for i in range(2, count+2):
        print(*list(range(i, count+i)))

main()
