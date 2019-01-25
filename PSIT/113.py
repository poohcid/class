"""psit"""

def main(many, dic_id, lst_id):
    """psit"""
    for _ in range(many):
        name = input().split("\t")
        dic_id.update({float(name[1]): int(name[0])})
        lst_id.append(float(name[1]))
    aver = sum(lst_id)/many
    for i in list(lst_id):
        if i > aver:
            lst_id.remove(i)
    answer = max(lst_id)
    print("%d\t%s" %(dic_id[answer], str(answer)))

main(int(input()), dict(), [])
