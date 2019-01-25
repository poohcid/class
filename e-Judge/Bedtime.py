"""Bedtime"""

def main():
    """function_main"""
    hour1 = int(input())
    minu1 = int(input())
    hour2 = int(input())
    minu2 = int(input())
    if hour1 < hour2:
        time = hour2-hour1-1
        time = time+((minu2-minu1) >= 0)
    elif hour1 > hour2:
        time = 24-(hour1-hour2)-1
        time = time+((minu2-minu1) >= 0)
    else:
        time = 24
    if time < 7:
        print("Not enough")
    elif time < 10:
        print("Enough")
    else:
        print("Too much")

main()
