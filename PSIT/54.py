"""[EX] PointInTriangle"""

def main():
    """find for finish 0 score"""
    kilo, minu = int(input()), int(input())
    total_1 = 35
    if kilo <= 1:
        total_1 += 0
    elif 1 < kilo <= 12:
        total_1 += (kilo-2+1)*5
    elif kilo <= 20:
        total_1 += 55 + (kilo-13+1)*5.50
    elif kilo <= 40:
        total_1 += 99 + (kilo-21+1)*6
    elif kilo <= 60:
        total_1 += 219 + (kilo-41+1)*6.50
    elif kilo <= 80:
        total_1 += 349 + (kilo-61+1)*7.50
    else:
        total_1 += 499 + (kilo-81+1)*8.50
    total_1 = round(total_1)
    total_1 += total_1%2 == 0
    total_2 = int(minu*1.50)
    total_2 -= total_2%2 == 1
    print(total_1+total_2)

main()
