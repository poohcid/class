"""Timing II"""

def main():
    """Function process and print"""
    time = int(input())
    times = time
    day = time//86400
    time = time%86400
    hour = time//3600
    time = time%3600
    minute = time//60
    sec = time%60
    if (day < 10000) and (times >= 0):
        print("%04d:%02d:%02d:%02d" %(day, hour, minute, sec))
    else:
        print("ERR_:__:__:__")

main()
