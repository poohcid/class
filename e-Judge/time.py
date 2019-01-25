"""time"""

def main():
    """function"""
    time = int(input())
    hour = time/3600
    time = (time%3600)
    minu = time/60
    time = (time%60)
    sec = time
    print("%d Hour(s) %d Minute(s) %d Second(s)" %(hour, minu, sec))
main()
