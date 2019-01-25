"""Energy"""

def main():
    """function"""
    distance = float(input())
    energy = int(input())
    pig = float(((((distance*1000)/10)/energy)))
    pigf = pig
    piece = pig%int(pigf)
    piecex = 0 < piece
    int(piecex)
    pig = int(pig)+piecex
    print("%d" %pig)
main()
