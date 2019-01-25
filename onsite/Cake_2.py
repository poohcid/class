"""Cake"""

def main(count):
    """main"""
    import math
    num1, num2 = int(input()), int(input())
    for _ in range(count-1):
        num3, num4 = int(input()), int(input())
        if num2 == num4:
            num1 = num1+num3
            num2 = num4
        else:
            stand = cranberry(num2, num4)
            num1 = num1*(stand//num2)
            num3 = num3*(stand//num4)
            num2, num4 = stand, stand
            num1 = num1+num3
    cake = math.ceil(num1/num2)
    if cake == (num1/num2):
        print("%d\n0" %cake)
    else:
        eated = divisor(num1, num2, cake)
        print("%d\n%s" %(cake, eated))

def cranberry(num1, num2):
    """precess_number_Cranberry"""
    num1, num2 = max(num1, num2), min(num1, num2)
    if num1%num2 == 0:
        total = num1
    else:
        count = 2
        while True:
            number = num1*count
            if number%num2 == 0:
                total = number
                break
            elif count == num2:
                total = num1*num2
                break
            else:
                count += 1
    return total

def divisor(num1, num2, cake):
    """process_last_divisor"""
    num1 = (cake*num2)-num1
    divi = num1
    while divi > 1:
        if (num1%divi == 0) and (num2%divi == 0):
            break
        else:
            divi -= 1
    num1, num2 = num1//divi, num2//divi
    return str(num1)+"/"+str(num2)

main(int(input()))
