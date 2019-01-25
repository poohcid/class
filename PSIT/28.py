"""Circular II"""

def main():
    """process hypot"""
    my_x, my_y = float(input()), float(input())
    my_radian = float(input())
    mos_x, mos_y = float(input()), float(input())
    mos_radian = float(input())

    #find distance
    num_x, num_y = abs(mos_x-my_x)**2, abs(mos_y-my_y)**2
    line = (num_x + num_y)**0.5

    #check radius 1 or 2 more than distance circular border
    if (my_radian <= (line-mos_radian)) or (mos_radian <= (line-my_radian)):
        print("No")
    else:
        print("Yes")

main()
