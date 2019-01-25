"""psit"""

def main(name, dic_id):
    """psit"""
    while name != "END":
        if name[0:2] not in dic_id:
            dic_id[name[0:2]] = [int(name[2:4])]
        else:
            dic_id[name[0:2]].append(int(name[2:4]))
        name = input()
    for i in sorted(tuple(dic_id.keys())):
        facu = list(sorted(tuple(set(dic_id[i]))))
        facu_id = facu.pop(0)
        print("%s %d %d" %(i, facu_id, dic_id[i].count(facu_id)))
        while len(facu) != 0:
            facu_id = facu.pop(0)
            print("-- %d %d" %(facu_id, dic_id[i].count(facu_id)))

main(input(), {})
