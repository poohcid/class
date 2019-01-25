"""Inflation"""

def main():
    """print money in futuer year"""
    price = float(input())
    percent = int(input())
    price = int((price*100)//1)
    for _ in range(percent):
        price += price*381//10000
    print("%d.%02d" %(price//100, price%100))

main()
