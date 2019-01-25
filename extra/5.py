"""Min Step to One"""

def main():
    """main"""
    many = int(input())
    for _ in range(many):
        number, count = int(input()), 0
        while number > 1:
            count += 1
            if number%2 == 0:
                number = number//2
            elif number%3 == 0:
                number = number//3
            else:
                number -= 1
        print(count)

main()
