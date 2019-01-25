"""Quadrant"""

def main():
    """main"""
    angle = int(input())
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    if (angle == 0) or (angle == 180):
        print("x-axis")
    elif (angle == 90) or (angle == 270):
        print("y-axis")
    elif angle > 270:
        print(4)
    elif angle > 180:
        print(3)
    elif angle > 90:
        print(2)
    else:
        print(1)

main()
