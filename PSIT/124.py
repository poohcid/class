"""psit"""

def main(number, check):
    """psit"""
    if number <= 2 or number%2 == 0:
        print(check if number == 2 else "NO")
    else:
        for i in range(3, int(number**0.5)+1, 2):
            print(i)
            if number%i == 0:
                check = "NO"
                break
        print(check)

main(int(input()), "YES")
