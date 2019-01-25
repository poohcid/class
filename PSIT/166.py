"""Ink"""
import math

def main():
    """Ink"""
    case = list(map(int, input().split()))
    for _ in range(case[-1]):
        home = list(map(int, input().split()))
        radius = (home[0]**2 + home[1]**2)**0.5
        area = 3.1416*radius**2
        print(math.ceil(area/case[0]))

main()
