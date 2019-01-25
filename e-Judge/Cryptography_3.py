"""Caesar N Cipher 2"""

def main():
    """main"""
    number = int(input())
    text = input()
    if text.isalpha():
        while number > 26:
            number -= 26
        total = ord(text)-number
        if 65 > total:
            total = 91-(65-total)
            print(chr(total))
        elif (total < 97) and (text.islower()):
            total = 123-(97-total)
            print(chr(total))
        else:
            print(chr(total))
    else:
        print(text)

main()
