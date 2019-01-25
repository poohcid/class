"""Direction"""

def main():
    """function_main"""
    numx = int(input())
    numy = int(input())
    if numx >= 0 and numy > 0:
        if numx == 0:
            print("North")
        else:
            print("Northeast")
    elif numx < 0 and numy >= 0:
        if numy == 0:
            print("West")
        else:
            print("Northwest")
    elif numx <= 0 and numy < 0:
        if numx == 0:
            print("South")
        else:
            print("Southwest")
    elif numx > 0 and numy <= 0:
        if numy == 0:
            print("East")
        else:
            print("Southeast")
    center(numx, numy)

def center(numx, numy):
    """Toomany"""
    if numx == 0 and numy == 0:
        print("Origin")

main()
