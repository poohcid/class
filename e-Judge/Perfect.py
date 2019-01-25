"""Perfect"""

def main():
    """function"""
    pear1 = int(input())
    pear2 = int(input())
    pear3 = int(input())
    num1 = max(pear1, pear2, pear3)
    num2 = min(pear1, pear2, pear3)
    total = pear1+pear2+pear3
    pear = total-(num1+num2)
    print(pear)

main()
