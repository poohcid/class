"""Label Number"""

def main():
    """main"""
    num_x, num_y = int(input()), int(input())
    text = ""
    for i in range(num_x, num_y+1):
        text += str(i)
    for i in range(10):
        print(text.count(str(i)), end=" ")

main()
