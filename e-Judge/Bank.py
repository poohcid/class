"""Bank"""

def main():
    """function"""
    baht = int(input())
    bank = (baht//1000)
    baht = (baht%1000)
    print(bank)
    bank = (baht//500)
    baht = (baht%500)
    print(bank)
    bank = (baht//100)
    baht = (baht%100)
    print(bank)
    bank = (baht//50)
    baht = (baht%50)
    print(bank)
    bank = (baht//20)
    baht = (baht%20)
    print(bank)
    bank = (baht//10)
    print(bank)
main()
