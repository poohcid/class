"""Fibonacci"""

def main():
    """Function_input_"""
    num = int(input())
    text = [0, 1, 1]
    for _ in range(2, num):
        text.append(text[-1]+text[-2])
    if num == 0:
        print(0)
    else:
        print(text[-1])

main()
