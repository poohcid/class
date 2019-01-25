"""SurprisingVote"""

def main():
    """find to low scroe for high socre"""
    total = float(input())
    high = float(input())
    #Use high score to calulate is get lows core
    check = (total - high) - high
    if (((high-check) <= 2) and (check >= 0)) or (high <= 2):
        print("Not surprising")
    else:
        print("Surprising")

main()
