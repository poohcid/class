"""Olympic problem"""
def olympic():
    """Print Olympic scoreboard."""
    count = int(input())
    rank_dic = [input().split() for _ in range(count)]
    rank_dic.sort(key=myfun, reverse=True)
    check, num = [], 1
    for i in rank_dic:
        if i[1:] == check:
            print(num, *i)
        else:
            num = rank_dic.index(i)+1
            print(num, *i)
            check = i[1:]

def myfun(lst):
    """myfun"""
    return int(lst[1]), int(lst[2]), int(lst[3]), list(map(lambda x: -ord(x), list(lst[0])))

olympic()
