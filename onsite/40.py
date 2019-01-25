"""BootSequence"""

def main():
    """print 1-10 one line add _"""
    count = int(input())
    print(1, end="")
    for i in range(2, count+1):
        print("_", end="")
        print(i, end="")

main()
