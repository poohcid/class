"""Matrix"""

def main():
    """function_main"""
    size = int(input())
    total = ""
    for _ in range(size):
        for _ in range(size):
            number = int(input())
            total += str(number)+" "
        total += "\n"
    print(total)

main()
