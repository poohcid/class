"""Sequence VIII"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    space, many = 1, count+(count-1)
    for i in range(1, count+1):
        for number in range(1, space):
            print("%02d" %number, end=" ")
        print(("%02d " %i)*many, end="")
        for number in range(space-1, 0, -1):
            print("%02d" %number, end=" ")
        print()
        space += 1
        many -= 2
    space -= 2
    many += 4
    for i in range(count-1, 0, -1):
        for number in range(1, space):
            print("%02d" %number, end=" ")
        print(("%02d " %i)*many, end="")
        for number in range(space-1, 0, -1):
            print("%02d" %number, end=" ")
        print()
        space -= 1
        many += 2
main()
