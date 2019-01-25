"""numday"""

def main():
    """numday"""
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = [[int(input()), int(input())], [int(input()), int(input())]]
    day.sort(key=lambda x: x[1])
    day1, month1 = day[0][0], day[0][1]
    day2, month2 = day[1][0], day[1][1]
    if day1 not in range(1, year[month1-1]+1) or day2 not in range(1, year[month2-1]+1):
        print("Impossible")
    elif month1 == month2:
        print(abs(day2-day1))
    else:
        print(abs(year[month1-1]-day1 + sum(year[month1:month2-1]) + day2))

main()
