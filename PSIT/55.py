"""[EX] PointInTriangle"""

def main():
    """find for finish 0 score"""
    var_c, var_f, var_x = float(input()), float(input()), float(input())
    cookie = 2
    total, total_1, total_2 = 0, var_x/cookie, var_c/cookie+var_x/(cookie+var_f)
    while total_1 > total_2:
        total += var_c/cookie
        cookie += var_f
        total_1 = total+var_x/(cookie)
        total_2 = total+var_c/(cookie)+var_x/(cookie+var_f)
    total += var_x/cookie
    print(int(total) if total == float(int(total)) else "%.4f" %total)

main()
