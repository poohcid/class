"""JOJO"""

def main():
    """main"""
    text = input().upper()
    text3 = text.split()
    if ("MUDA" in text3) or ("ORA" in text3):
        text1 = text.split()
        text2 = text.split()
        while "ORA" in text1:
            text1.remove("ORA")
        while "MUDA" in text2:
            text2.remove("MUDA")
        if "MUDA" in text1:
            print(*text1)
        if "ORA" in text2:
            print(*text2)
        if len(text1) > len(text2):
            print("GOODBYE JOJO!")
        elif len(text1) < len(text2):
            print("Yare Yare Daze")
        else:
            print("WR"+"Y"*len(text1))
    else:
        print("Menacing")

main()
