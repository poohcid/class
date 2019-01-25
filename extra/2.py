"""ThreeSUM"""

def main(number):
    """Function_input_"""
    many = 0
    for count in range(number, 0, -1):
        many += count
    name1, name2, name3 = input(), input(), input()
    around, count = 0, 1
    while count <= many:
        around += 1
        if around == 4:
            around = 1
        count += 1
    if around == 1:
        print("Winner is %s!!" %name1)
    elif around == 2:
        print("Winner is %s!!" %name2)
    elif around == 3:
        print("Winner is %s!!" %name3)

main(int(input()))
