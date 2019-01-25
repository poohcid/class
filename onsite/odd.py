"""Even_Odd"""

def main():
    """Function_input_"""
    stop = int(input())
    number = 2
    while number <= stop:
        divi = 3
        if number == 2:
            print(2)
            number += 1
            continue
        elif number%2 != 0:
            while True:
                count = number%divi
                if (count == 0) and (number == divi):
                    print(number)
                    break
                elif (count == 0) and (number != divi):
                    break
                elif count != 0:
                    divi += 2
        number += 2

main()
