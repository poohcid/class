"""Cards"""

def main():
    """main"""
    many = int(input())
    card, score = "", 0
    for around in range(many):
        if (around+1) == many:
            card += input()
        else:
            card += input()+","
    while True:
        cardf = card_change(card)
        if len(cardf) != len(card):
            break
        else:
            score += 1
            card = cardf
            print(card)
    print(score)

def last_card(card):
    """return_last_number"""
    text = ""
    for count in card:
        if count != ",":
            text += count
        else:
            text = ""
    number = int(text)
    return number

def card_stack(card, num1, digit):
    """return_stand_card"""
    text, around, add = "", 1, 0
    for count in card:
        if count == ",":
            around += 1
        if (around == digit) and (count != ","):
            if add == 0:
                text += str(num1)+","+count
                add = 1
            else:
                text += count
        else:
            text += count
        if len(text) == len(card):
            break
    return text

def card_change(card):
    """change_card"""
    text, add = "", 999999.5
    add_pow, around = 999999.5, 0
    number = last_card(card)
    for count in card:
        if count != ",":
                text += count
        else:
            count = int(text)
            text = ""
            around += 1
            if (number < count) and ((count-number) < add):
                add = count-number
                digit = around
            elif (number > count) and ((number-count) < add_pow) and \
            (add == 999999.5):
                add_pow = number-count
                digit = around
    if add != 999999.5:
        return card_stack(card, number, digit)
    else:
        return card_stack(card, number, digit+1)

main()
