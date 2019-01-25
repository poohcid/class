"""Circular I"""

def main():
    """the radius more than a distance is mosquito in the area"""
    my_x, my_y = float(input()), float(input())
    radian = float(input())
    mos_x, mos_y = float(input()), float(input())
    #calculate to distance
    num_x, num_y = abs(mos_x-my_x)**2, abs(mos_y-my_y)**2
    line = (num_x + num_y)**0.5
    if line <= radian:
        print("Yes")
    else:
        print("No")

main()
