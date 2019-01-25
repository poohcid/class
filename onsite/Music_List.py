"""Music_List"""

def main():
    """main"""
    text, text1 = input(), []
    text2 = []
    text = text.split(", ")
    for i in text:
        if i.upper() not in text2:
            text1.append([len(i), i])
            text2.append(i.upper())
    text1.sort(reverse=True)
    for i in range(len(text1)):
        print("%d.%s" %(i+1, text1[i][1]))

main()
