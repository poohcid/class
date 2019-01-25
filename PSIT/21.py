"""WeightStation"""

def main():
    """condition to statement"""
    average, num1 = float(input()), float(input())
    num2, num3 = float(input()), float(input())
    num4 = (average*4) - (num1+num2+num3)
    total = num1+num2+num3+num4
    if total <= 15000:
        aver1 = average - (average/2)
        aver2 = average + (average/2)
        con1 = (aver1 <= num1 <= aver2) and (aver1 <= num2 <= aver2)
        con2 = (aver1 <= num3 <= aver2) and (aver1 <= num4 <= aver2)
        if con1 and con2:
            print("Pass %.2f" %num4)
        else:
            print("Unbalance")
    else:
        print("Overweight")

main()
