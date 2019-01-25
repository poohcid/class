"""Run Length Decoding"""

def main():
    """Run Length Decoding"""
    text = input()
    number = ""
    for i in text:
        if i.isdigit():
            number += i
        else:
            print(i*int(number), end="")
            number = ""

main()
