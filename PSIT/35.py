"""Gift III"""

def main():
    """print second nunber"""
    many = int(input())
    box1, box2 = 0, 0
    for _ in range(many):
        box = int(input())
        if box > box1:
            box1, box2 = box, box1
        elif (box > box2) and (box != box1):
            box2 = box
        elif (box < box1) and (box2 == box1):
            box2 = box
    if box2 == 0:
        print("Exit")
    else:
        print(box2)

main()
