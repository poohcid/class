"""Camp_4"""

def main():
    """main"""
    name  = input()
    total = ""
    for text in name:
        if 97 <= ord(text) <= 122:
            total += chr(text-32)
        else:
            total += text
    print(text)

main()
