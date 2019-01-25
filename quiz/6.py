"""Wallet Capacity"""

def main():
    """Function"""
    bath = int(input())
    many = int(input())
    total = 0
    total += bath//1000
    bath = bath%1000
    total += bath//500
    bath = bath%500
    total += bath//100
    bath = bath%100
    total += bath//50
    bath = bath%50
    total += bath//20
    if total <= many:
        print("Yes")
    else:
        print("No")

main()
