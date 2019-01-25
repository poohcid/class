"""Diamond I"""

def main():
    """Diamond I"""
    var_m, var_n = int(input()), int(input())
    dic_level = []
    for _ in range(var_m):
        ore = list(map(int, input().split()))
        dic_level.append(ore)
    lst_ore = []
    for i in range(var_n):
        ore = []
        for j in range(var_m):
            ore.append(dic_level[j][i])
        lst_ore.append(ore)
    result = max(lst_ore, key=sum)
    print(sum(result))

main()
