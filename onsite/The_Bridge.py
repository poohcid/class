"""The_Bridge"""

def main():
    """main"""
    text = ["Austria", "Belgium", "Bulgaria", "Croatia",\
    "Cyprus", "Denmark", "Estonia", "Finland", "France",\
    "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania",\
    "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania",\
    "Slovakia", "Slovenia", "Spain", "Sweden"]
    extra = ["Czech republic", "United kingdom"]
    many, name = int(input()), []
    for _ in range(many):
        text1, text2 = input().capitalize(), input().capitalize()
        text4 = ""
        text1 = text1.split()
        for i in text1:
            text4 += i.capitalize()+" "
        text1 = text4.split()
        digit = ord(text1[0][0])
        text3 = input().capitalize()
        if text3 in text:
            name.append([digit, text1, text2, text3])
        if text3 in extra:
            text3 = text3.split()
            text3 = text3[0]+" "+text3[1].capitalize()
            name.append([digit, text1, text2, text3])
    name.sort()
    for i in name:
        del i[0]
        print(*i[0], end="")
        print(" in %s, %s" %(i[1], i[2]))

main()
