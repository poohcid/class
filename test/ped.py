"""PedPonFire"""

def main():
    """PedPonFire"""
    count = int(input()) - 1
    lst_ped = [int(input())]
    dic_ped = {}
    for i in range(count):
        ped = int(input())
        for j in range(len(lst_ped)):
            result = lst_ped[j] + ped
            if result not in dic_ped:
                dic_ped[result] = 1
            else:
                dic_ped[result] += 1
        lst_ped.append(ped)
    gass = int(input())
    print(dic_ped[gass] if gass in dic_ped else 0)

main()
