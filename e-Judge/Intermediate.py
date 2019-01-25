"""Intermediate"""

def main():
    """function_main"""
    name = input()
    name = ord(name)-6
    if name < 65:
        name = 90-(64-name)
    elif 90 < name < 97:
        name = 122-(96-name)
    print(chr(name))

main()
