"""Still_Sleepy"""

def main():
    """function_main"""
    hour = int(input())
    minu = int(input())
    if hour >= 9:
        print("Continued sleeping")
    else:
        if hour >= 8 and minu >= 15:
            time = 65-33
        elif hour >= 8:
            time = 65-25
        elif hour >= 7 and minu >= 45:
            time = 65-16
        elif hour >= 7 and minu >= 30:
            time = 65-10
        else:
            time = 65
        hourf = hour+(time//60)+((minu+(time%60)) >= 60)
        minuf = (minu+(time%60))%60
        print("%02d:%02d - %02d:%02d (Time Used: %d Hour(s) %d Minute(s))"\
        %(hour, minu, hourf, minuf, time//60, time%60))

main()
