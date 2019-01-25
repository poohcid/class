"""FibonacciRecursionV2"""

def main(count):
    """FibonacciRecursionV2"""
    #if count >= 100:
        #fibo2(218922995834555169026, 354224848179261915075, count-100, 0)
    #else:
    fibo2(1, 0, count, 0)

def fibo2(num1, num2, count, around):
    """fibo2"""
    if count == 0:
        print(num2)
        return 0, 0, 0, "END"
    elif around == 100:
        return num2, num1 + num2, count-1, around-1
    else:
        num1, num2, count, around = fibo2(num2, num1+num2, count-1, around + 1)
        if around == "END":
            return 0, 0, 0, "END"
        if around != 0 and count == 0:
            print(num2)
            return 0, 0, 0, "END"
        elif around != 0:
            return num2, num1+num2, count-1, around-1
        elif around == 0:
            fibo2(num1, num2, count, around)

main(int(input()))
