"""Remainder"""

def main():
    """function_main"""
    numa = int(input()) #a
    numb = int(input()) #b
    step = -1
    if numa < 0:
        step = 1
    for numa in range(numa, 0, step):
        check = numa%numb
        if check == 0:
            print(numa)

main()
