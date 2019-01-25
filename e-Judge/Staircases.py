"""Staircases"""

def main():
    """function_main"""
    high = int(input())
    line = 1
    for _ in range(high):
        print("*"*line, end="\n")
        line += 1

main()
