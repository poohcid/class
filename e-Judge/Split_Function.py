"""Split_Function"""

def main():
    """function_main"""
    import math
    num = float(input())
    if num < 100:
        total = 2*math.sin(((num-10)*math.pi)/180)
    elif num == 100:
        total = math.sqrt(num)/5
    else:
        total = math.log10(num)
    print("%.2f" %total)

main()
