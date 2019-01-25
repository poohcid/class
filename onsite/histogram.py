"""histogram"""

def main():
    """main"""
    text = input()
    chara = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    name, most = "", 0
    for i in chara:
        if i in text:
            most = max(text.count(i), most)
            name += i
    for i in chara.lower():
        if i in text:
            most = max(text.count(i), most)
            name += i
    for i in range(most, 0, -1):
        print("{:>{}}" .format(i, 2), end="  ")
        for key in name:
            if text.count(key) >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n", end="")
    print("   ", end=" ")
    for i in name:
        print(i, end=" ")

main()
