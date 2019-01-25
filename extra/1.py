"""Store"""

def main(many, price):
    """Function_input_"""
    total = price
    if many > 15:
        total -= (price%10)
    elif many > 10:
        total -= 5
    if total > 300:
        total -= 20
    elif total > 150:
        total -= 10
    else:
        total -= 1
    if total <= 1000:
        print(1000-total)
    else:
        print("Not enough money")

main(int(input()), int(input()))
