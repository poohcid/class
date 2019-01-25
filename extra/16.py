"""Butterfly"""

def main():
    """main"""
    text = input()
    size = int(input())
    space = size
    for i in range(size//2-1):
        space -= 2
        print(text*(i+1)+" "*space+text*(i+1))
    print(text*size)
    for i in range(size//2-1, 0, -1):
        print(text*(i)+" "*space+text*(i))
        space += 2

main()
