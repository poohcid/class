"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""

def main():
    """sort"""
    text, num1 = input(), float(input())
    num2, num3 = float(input()), float(input())
    num1, num2 = high(num1, num2), lower(num1, num2)
    num1, num3 = high(num1, num3), lower(num1, num3) #num1 highest
    num2, num3 = high(num2, num3), lower(num2, num3) #num2 more than num3
    if text == "Ascend":
        print("%.2f, %.2f, %.2f" %(num3, num2, num1))
    elif text == "Descend":
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))

def high(num1, num2):
    """return number highest"""
    if num1 > num2:
        return num1
    else:
        return num2

def lower(num1, num2):
    """return number lower"""
    if num1 < num2:
        return num1
    else:
        return num2

main()
