"""How Long"""

def main():
    """main"""
    time = int(input())
    print("%dYear" %(time//31104000), end="")
    print("s"*(time//31104000 > 1), end=" ")
    time = time%31104000
    print("%dMonth" %(time//2592000), end="")
    print("s"*(time//2592000 > 1), end=" ")
    time = time%2592000
    print("%dDay" %(time//86400), end="")
    print("s"*(time//86400 > 1), end=" ")
    time = time%86400
    print("%dHour" %(time//3600), end="")
    print("s"*(time//3600 > 1), end=" ")
    time = time%3600
    print("%dMinute" %(time//60), end="")
    print("s"*(time//60 > 1), end=" ")
    time = time%60
    print("%dSecond" %time, end="")
    print("s"*(time > 1))

main()
