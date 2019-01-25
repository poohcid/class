"""RuleofThree"""

def main():
    """total Worth"""
    many = int(input())
    candy, price, weight = 0, 0, 0
    for _ in range(many):
        price2, weight2 = float(input()), float(input())
        if candy < weight2/price2:
            price, weight = price2, weight2
            candy = weight/price
        elif candy == weight2/price2:
            if price2 < price:
                price, weight = price2, weight2
            candy = weight/price
    print("%.2f %.2f" %(price, weight))

main()
