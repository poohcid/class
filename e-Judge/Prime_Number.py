"""Prime_Number"""

def main():
    """function_main"""
    number = int(input())
    if number == 1 or number == 0 or number < 0:
        print("No")
    elif number == 2:
        print("Yes")
    elif (number%2) == 0:
        print("No")
    else:
        divi = 3 #divi is divisor
        while divi <= number:
            total = number%divi
            if total == 0 and number != divi:
                print("No")
                break
            elif number == divi:
                print("Yes")
                break
            else:
                divi += 1

main()
