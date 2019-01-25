"""Matrix"""

def main():
    """function_main"""
    size = int(input())
    total = ""
    if size == 1:
        print(input())
    else:
        for _ in range(size):
            space = " "
            for around in range(size):
                if around == size-1:
                    space = ""
                total += input()+space
            total += "\n"
        print(total)

main()
