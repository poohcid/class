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
    lst_island = [{lst_point.pop(0)}] if lst_point else []
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
    #print(*lst_island, sep="\n")
    many = []
    while lst_island:
        island = lst_island.pop(0)
        for i in list(lst_island):
            if island & i:
                island = island | i
                lst_island.remove(i)
                #print(lst_island)
        many.append(island)
    #print("___", *many, sep="\n")
    return len(many) if many else 0
def set_point(point):
    """return set point"""
    return {point, (point[0]-1, point[1]-1), (point[0], point[1]-1), (point[0]+1, point[1]-1), \
    (point[0]-1, point[1]), (point[0]+1, point[1]), (point[0]-1, point[1]+1), \
    (point[0], point[1]+1), (point[0]+1, point[1]+1)}

print(main())
