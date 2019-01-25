"""Average"""

def main():
    """function_main"""
    many = int(input())
    weight = 0
    total = 0
    for _ in range(1, many+1):
        weight = float(input())
        total += weight
    print("Average is %.2f" %(total/many))

main()
