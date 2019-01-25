"""Caesar N Cipher 2"""

def main():
    """main"""
    number = int(input())
    text = input()
    for i in text:
        if i.isalpha():
            while number > 26:
                number -= 26
            total = ord(i)-number
            if total < 65:
                total = 91-(65-total)
                print(chr(total), end="")
            elif (total < 97) and (i.islower()):
                total = 123-(97-total)
                print(chr(total), end="")
            else:
                print(chr(total), end="")
        else:
            print(i, end="")

main()
