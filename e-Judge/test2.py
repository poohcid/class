"""Pre-Pro 61 - Sample Code"""

def main():
    """Sort"""
    num1 = float(input())
    num2 = float(input())
    from math import pi, sin, cos, floor,sqrt
    deg = (num2*pi)/180
    tol1 = floor(num1*cos(deg))
    tol2 = floor(sqrt((num2**3)+sqrt((num2*sin(pi/3))+sqrt(num2))))
    total = -abs(tol1-tol2)
    print(total)
main()
