"""Inflation"""

def main():
    """print money in futuer year"""
    price = float(input())
    percent = int(input())
    price = ((price*100)//1)*0.01
    add_money = price*(3.81/100)
    for _ in range(percent):
        #add_money = price*(3.81/100)
        price += add_money
        price = ((price*100)//1)*0.01
    print("%.2f" %price)

main()
