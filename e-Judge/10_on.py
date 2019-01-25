"""Dots"""

def main():
    """main"""
    num_ax, num_ay = int(input()), int(input())
    num_bx, num_by = int(input()), int(input())
    line = dots(num_bx-num_ax, num_by-num_ay) #a-b
    num_cx, num_cy = int(input()), int(input())
    line += dots(num_cx-num_bx, num_cy-num_by) #b-c
    num_dx, num_dy = int(input()), int(input())
    line += dots(num_dx-num_cx, num_dy-num_cy) #c-d
    line += dots(num_ax-num_dx, num_ay-num_dy) #d-a
    print("%.2f" %line)

def dots(num_x, num_y):
    """process_to_long"""
    import math
    total = math.hypot(abs(num_x), abs(num_y))
    return total

main()
