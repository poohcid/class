"""Cake"""

def main(count, total):
    """main"""
    import math
    for _ in range(count):
        total += int(input())/int(input())
    cake = math.ceil(total)
    eated = cake_f(cake-total)
    print("%d\n%s" %(cake, eated))

def cake_f(cake):
    """process_cake"""
    if len(str(cake)) >= 18:
        return "unknow"
    else:
        piece = int(cake*100)
        divi = divisor(int(cake*100), 100)
        text = str(int(piece/divi))+"/"+str(int(100/divi))
        return text

def divisor(num1, num2):
    """process_last_divisor"""
    num1, num2 = min(num1, num2), max(num1, num2)
    divi = num1
    while divi > 1:
        if (num1%divi == 0) and (num2%divi == 0):
            break
        else:
            divi -= 1
    return divi


main(int(input()), 0)
