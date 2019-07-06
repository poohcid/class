"""doc"""

def main():
    """doc"""
    text = input()
    lisnum = []
    listext = []
    text1 = ""
    num = ""
    for i in text:
        if i.isdigit():
            num += i
        elif i == "%":
            listext.extend([text1, i])
            lisnum.append(num)
            text1, num = "", ""
        elif not i.isdigit():
            if num:
                lisnum.append(num)
                num = ""
            if i.isupper():
                listext.append(text1)
                text1 = ""
            text1 += i
    listext.append(text1)
    lisnum.append(num)
    while '' in listext:
        listext.remove('')
    while '' in lisnum:
        lisnum.remove('')
    for i in listext:
        if i == '%':
            print(lisnum.pop(0), end=" ")
        else:
            print(i, end=" ")
    print()

main()