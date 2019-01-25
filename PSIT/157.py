"""Island"""

def main():
    """Island"""
    roll, collum = list(map(int, input().split()))
    lst_point = []
    for i in range(roll):
        island = input().split()
        for j in range(collum):
            if island[j] == "1":
                lst_point.append((j, i))
    if len(lst_point) == 0:
        return 0
    lst_island = [{lst_point.pop(0)}]
    while len(lst_point) != 0:
        point = lst_point.pop(0)
        side = set_point(point)
        check = 0
        for i in range(len(lst_island)):
            if len(lst_island[i] & side) > 0:
                lst_island[i] = lst_island[i] | {point}
                check = 1
        if check == 0:
            lst_island.append({point})
    total = []
    for i in range(len(lst_island)):
        for j in range(i+1, len(lst_island)):
            point1 = lst_island[i]
            point2 = lst_island[j]
            if point1 & point2:
                lst_island[i] = lst_island[i] | lst_island[j]
                del lst_island[j]
    return len(lst_island)
def set_point(point):
    """return set point"""
    return {point, (point[0]-1, point[1]-1), (point[0], point[1]-1), (point[0]+1, point[1]-1), \
    (point[0]-1, point[1]), (point[0]+1, point[1]), (point[0]-1, point[1]+1), \
    (point[0], point[1]+1), (point[0]+1, point[1]+1)}

print(main())
