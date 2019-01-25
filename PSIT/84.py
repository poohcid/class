"""Largest Number"""

def main(num1, num2, num3):
    """statement"""
    num1, num2 = high(num1, num2)
    num1, num3 = high(num1, num3)
    num2, num3 = high(num2, num3)
    print(int(num1+num2+num3))

def high(num1, num2):
    """high"""
    add = 1
    count1, count2 = num1[0], num2[0]
    while (count1 == count2) and ((add < len(num1)) and (add < len(num2))):
        add += 1
        count1, count2 = num1[add], num2[add]
    if (count1 >= count2) and (len(num1) <= len(num2)):
        return num1, num2
    else:
        return num2, num1

main(str(int(input())), str(int(input())), str(int(input())))
