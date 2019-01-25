"""Which_Case"""

def main():
    """main"""
    name, add, total = input(), 0, ""
    for text in name:
        if text.isalpha():
            if (97 <= ord(text) <= 122) and (add == 0):
                total += text.upper()
                add = 1
            else:
                total += text
    print(total)

main()
