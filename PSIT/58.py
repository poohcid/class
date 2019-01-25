"""[EX] PointInTriangle"""
import math

def main():
    """find for finish 0 score"""
    x_1, y_1 = float(input()), float(input())
    x_2, y_2 = float(input()), float(input())
    x_3, y_3 = float(input()), float(input())
    dotx, doty = float(input()), float(input())

    #the large triangle
    line1 = line_long(x_1, y_1, x_2, y_2)
    line2 = line_long(x_2, y_2, x_3, y_3)
    line3 = line_long(x_3, y_3, x_1, y_1)
    total_all = area(line1, line2, line3)

    #the triangle 1
    total_1 = area(line_long(x_1, y_1, dotx, doty), \
    line_long(dotx, doty, x_2, y_2), line_long(x_1, y_1, x_2, y_2))
    if total_1 == 0:
        return condit(line_long(dotx, doty, x_1, y_1), \
        line_long(x_1, y_1, x_2, y_2), line_long(dotx, doty, x_2, y_2))

    #the triangle 2
    total_2 = area(line_long(x_2, y_2, dotx, doty), \
    line_long(dotx, doty, x_3, y_3), line_long(x_3, y_3, x_2, y_2))
    if total_2 == 0:
        return condit(line_long(dotx, doty, x_2, y_2), \
        line_long(x_2, y_2, x_3, y_3), line_long(dotx, doty, x_3, y_3))
    total_1 += total_2

    #the triangle 3
    total_2 = area(line_long(x_3, y_3, dotx, doty), \
    line_long(dotx, doty, x_1, y_1), line_long(x_1, y_1, x_3, y_3))
    if total_2 == 0:
        return condit(line_long(dotx, doty, x_3, y_3), \
        line_long(x_3, y_3, x_1, y_1), line_long(dotx, doty, x_1, y_1))
    total_1 += total_2

    #check statement
    if round(total_all) < round(total_1):
        return "out"
    else:
        return "in"

def line_long(numx, numy, dotx, doty):
    """return total line"""
    return math.hypot((numx-dotx), (numy-doty))

def area(line1, line2, line3):
    """return area"""
    var_s = (line1+line2+line3)/2
    return math.sqrt(abs(var_s*(var_s-line1)*(var_s-line2)*(var_s-line3)))

def condit(var_1, var_2, var_3):
    """if dot on line triangle"""
    text = "out"
    if (var_1 <= var_2) and (var_2 >= var_3):
        text = "on"
    return text

print(main())
