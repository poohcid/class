"""Kabata"""

def kabata(text):
    """Kabata"""
    check = "yes"
    while len(text) != 0:
        if text[:4] == "baka":
            check = "no"
            break
        elif text[:5] == "bakka":
            text = text[5:]
        elif text[:2] in ["ka", "ba", "ta"]:
            text = text[2:]
        else:
            check = "no"
            break
    print(check)

def main(count):
    """main loop"""
    for _ in range(count):
        kabata(input())

main(int(input()))
