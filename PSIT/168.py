"""Parallelogram"""

def main():
    """Parallelogram"""
    text = input()
    for i in range(len(text)):
        print(" "*(len(text)-i-1)+text[:i+1])
    for i in range(len(text)-1):
        print(text[i+1:])

main()
