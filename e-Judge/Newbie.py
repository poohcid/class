"""Newbie"""

def main():
    """function"""
    name = input()
    num = ord(name)
    num = (num-(25*(num == 90 or num == 122)))+\
    (num != 90 and num != 122)
    print(chr(num))

main()
