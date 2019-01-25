"""Alpha"""

def main():
    """function_main"""
    mail = input()
    for name in mail:
        if 90 >= ord(name) >= 65:
            print("*"*(ord(name)-64))
        elif ord(name) >= 97:
            print("*"*(ord(name)-96))
        else:
            print(" ")

main()
