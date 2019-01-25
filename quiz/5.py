"""Contest"""

def main():
    """Function"""
    number = int(input())
    total = 1
    for i in range(number, 1, -1):
        total *= i
    print(total)

main()
