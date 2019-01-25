"""SceneSwitch I"""

def main():
    """print time Switchable state: Warmwhite"""
    #fisrt step light ---> ON, color ----> cool
    #light 0 is off 1 is on value is state
    #color Cool is 1 Warmwhite is 2 value is count
    time1, count, state, warmwhite = input(), 1, 1, 0
    if time1 == "End": #time1 is end print 0
        time1 = -1
    else:
        time1 = int(time1)
    while time1 != -1:
        switch = input()
        if switch == "End":
            break
        time2 = float(switch)
        # every time you input change switch
        if state == 1:
            state = 0
        elif state == 0: #after step is ligh off
            time = time2 - time1
            # time long than 6 sec not cool to warm
            if time <= 6:
                #cool to warm
                count += 1
            else:
                # cool to cool
                count = 1
            state = 1
        if count == 2:
            warmwhite += 1
            #set value to next step
            count = 0
        #set value to next next step
        time1 = time2
    print(warmwhite)

main()
