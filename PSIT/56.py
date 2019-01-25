"""[EX] PointInTriangle"""

def main():
    """find for finish 0 score"""
    hour, minu = int(input())*5, int(input())
    hour += (1/12)*minu
    print(0 <= (hour - minu) < 1)

main()
