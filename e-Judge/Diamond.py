"""Diamond"""

def main():
    """function_main"""
    high = int(input())
    space = int(high/2)
    star = 1
    for around in range(high):
        print(" "*space+"*"*star, end="\n")
        if around >= int(high/2):
            space += 1
            star -= 2
        else:
            space -= 1
            star += 2

main()
