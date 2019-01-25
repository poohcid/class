"""RectangleArea"""

def main():
    """RectangleArea"""
    var_a = list(map(int, input().split()))
    var_b = list(map(int, input().split()))
    line_ax = set(range(var_a[0], var_a[0]+var_a[2]))
    line_ay = set(range(var_a[1], var_a[1]+var_a[3]))
    line_bx = set(range(var_b[0], var_b[0]+var_b[2]))
    line_by = set(range(var_b[1], var_b[1]+var_b[3]))
    line_x = line_ax & line_bx
    line_y = line_ay & line_by
    print(len(line_x)*len(line_y) if bool(line_x) and bool(line_y) else "no overlapping")

main()
