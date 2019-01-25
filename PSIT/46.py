"""Sequence VI"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    for i in range(1, count+1):
        print(*list(range(1, i+1)))

main()
