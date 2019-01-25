"""Airport"""

def main():
    """main"""
    select = input()
    if select == "A":
        plan(160)
    elif select == "B":
        plan(140)
    elif select == "C":
        plan(115)

def plan(time):
    """plan_A"""
    hour = int(input())
    minu = int(input())
    day = input() #day is am/pm
    total = ((hour*60)+minu)-time
    if (day == "am") and (total < 0): #minus over am
        total = 720-abs(total)
        day = "pm"
    if day == "pm": #minus over pm
        if (total < 720) and (hour >= 12): #minus over 12pm
            day = "am"
        if 0 <= total < 60: #minus 1am to 12.xx pm
            total = 720+total
        if total < 0:
            total = 720-abs(total) #minus over pm
            day = "am"
    hour = total//60
    minu = total%60
    print("%02d:%02d%s" %(hour, minu, day))

main()
