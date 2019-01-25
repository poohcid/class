"""Day2011"""

def main(day, month):
    """Day2011"""
    week = ["#", "Sunday", "Monday", "Tuesday", "Wednesday", \
    "Thursday", "Friday", "Saturday"]
    start_day = ["#", 6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    result = (day%7 + start_day[month])%7
    result = result*(result != 0) + 7*(result == 0)
    print(week[result])

main(int(input()), int(input()))
