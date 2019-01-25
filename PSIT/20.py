"""Gift I"""

def main():
    """Function process and print"""
    result = more(int(input()), more(int(input()), 0))
    result = more(int(input()), more(int(input()), result))
    result = more(int(input()), more(int(input()), result))
    result = more(int(input()), more(int(input()), result))
    print(result)

def more(num1, num2):
    """more than to return"""
    if num1 >= num2:
        return num1
    else:
        return num2

main()
