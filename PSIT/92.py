"""CoPrimeV1"""

def main():
    """CoPrimeV1"""
    num1 = int(input())
    num2 = int(input())
    divi = gcd_divisor(num1, num2)
    if divi == 1:
        print("YES", divi, sep="\n")
    else:
        print("NO", divi, sep="\n")

def gcd_divisor(num1, num2):
    """gcd"""
    if num1 == 0 or num2 == 0:
        divi = max(num1, num2)
    else:
        divi = min(num1, num2)
    while divi != 1:
        if num1%divi == 0 and num2%divi == 0:
            break
        else:
            divi -= 1
    return divi

main()
