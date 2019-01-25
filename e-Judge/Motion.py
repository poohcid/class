"""Motion"""

def main():
    """function"""
    import math
    speed = float(input())
    angle = float(input())
    rad = (angle*math.pi)/180
    radf = rad*2
    time = (2*speed*math.sin(rad))/9.8
    high = (math.pow(speed, 2)*math.pow(math.sin(rad), 2))/(9.8*2)
    radar = (math.pow(speed, 2)*math.sin(radf))/9.8
    print("t = %.2f" %time)
    print("H = %.2f" %high)
    print("R = %.2f" %radar)

main()
