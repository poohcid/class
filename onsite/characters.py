"""characters"""

def main():
    """main"""
    text = input()
    chara = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    name, most = "", 0
    for i in chara:
        if i in text:
            most = max(text.count(i), most)
            name += i
        elif i.lower() in text:
            most = max(text.count(i.lower()), most)
            name += i
    print(most, name)

main()
