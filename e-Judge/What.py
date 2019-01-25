"""What"""

def main():
    """function"""
    import math
    values = float(input())
    angle = float(input())
    rad = angle*(math.pi/180)
    sqr = math.sqrt(angle)
    sqr = (angle*math.sin(1.0472)+sqr)**0.5
    sqr = ((angle**3)+sqr)**0.5
    total = (values*math.cos(rad))-sqr
    total = abs(total)*(-1)
    print("%d" %int(total))

main()
