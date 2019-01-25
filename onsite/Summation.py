"""Summation"""

def main():
    """Function_input_"""
    count = int(input())
    total = 0
    for _ in range(count):
        total += float(input())
    print("%.4f" %total)

main()
