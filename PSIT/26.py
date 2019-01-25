"""366 days"""

def main():
    """process to 366 days in year"""
    year = int(input())
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print("Yes")
    else:
        print("No")

main()
