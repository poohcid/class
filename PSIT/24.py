"""Triangle I"""

def main():
    """process find normal triangle"""
    line1 = float(input())
    line2 = float(input())
    line3 = float(input())
    line1, line2 = high(line1, line2)
    line1, line3 = high(line1, line3)
    line2, line3 = high(line2, line3)
    total = (line2**2 + line3**2)**0.5
    if (total == line1) or (abs(line1 - total) <= 0.01):
        print("Yes")
    else:
        print("No")

def high(num1, num2):
    """return sorted numbers"""
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1

main()
