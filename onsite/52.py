"""Sequence VIII"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    count1 = count
    for i in range(1, count+1):
        for number in range(count1, count):
            print("%02d" %number, end=" ")
        for number in range(count, i-1, -1):
            print("%02d" %number, end=" ")
        for number in range(i+1, count+1):
            print("%02d" %number, end=" ")
        for number in range(count-1, count-i, -1):
            print("%02d" %number, end=" ")
        print()
        count1 -= 1
    count1 += 2
    for i in range(count-1, 0, -1):
        for number in range(count1, count):
            print("%02d" %number, end=" ")
        for number in range(count, i-1, -1):
            print("%02d" %number, end=" ")
        for number in range(i+1, count+1):
            print("%02d" %number, end=" ")
        for number in range(count-1, count-i, -1):
            print("%02d" %number, end=" ")
        print()
        count1 += 1

main()
