"""Vending"""

def main():
    """Function_input_"""
    total, price = 0, 0
    while True:
        text = input()
        if text == "END":
            break
        else:
            number = int(text)
            if number > 0:
                price += number
            elif price >= abs(number):
                price -= abs(number)
                total += 1
            else:
                print("ERROR: Not enough money for this item.")
    print("Items: %d" %total)
    print("Change: %d THB" %price)

main()
