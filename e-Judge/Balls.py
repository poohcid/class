"""Balls"""

def main():
    """function"""
    import math
    line = float(input())
    line = line/2
    area = 4*math.pi*(line**2)
    volume = (4/3)*math.pi*(line**3)
    print("A = %.3f" %area)
    print("V = %.3f" %volume)

main()
