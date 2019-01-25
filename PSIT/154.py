"""Point Sorting"""

def main():
    """Point Sorting"""
    for _ in range(int(input())):
        count = int(input())
        lst_point = [input().split() for _ in range(count)]
        for i in range(len(lst_point)):
            for j in range(i+1, len(lst_point)):
                change = b_sort(lst_point[i], lst_point[j])
                lst_point[i] = change[0]
                lst_point[j] = change[1]
        for i in lst_point:
            print(*i)

def b_sort(point1, point2):
    """sort"""
    point1, point2 = list(map(int, point1)), list(map(int, point2))
    if sum(point1) == sum(point2):
        if point2[1] > point1[1]:
            point1, point2 = point2, point1
    elif sum(point1) > sum(point2):
        point1, point2 = point2, point1
    return point1, point2

main()
