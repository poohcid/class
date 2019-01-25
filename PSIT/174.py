"""ProgressiveTax"""

def main():
    """ProgressiveTax"""
    money = int(input())
    total = 0
    if money > 4000000:
        total += (money - 4000000)*(0.35)
    if money > 2000000:
        total += (min(money, 4000000) - 2000000)*(0.3)
    if money > 1000000:
        total += (min(money, 2000000) - 1000000)*(0.25)
    if money > 750000:
        total += (min(money, 1000000) - 750000)*(0.2)
    if money > 500000:
        total += (min(money, 750000) - 500000)*(0.15)
    if money > 300000:
        total += (min(money, 500000) - 300000)*(0.1)
    if money > 150000:
        total += (min(money, 300000) - 150000)*(0.05)
    print(int(total))

main()
