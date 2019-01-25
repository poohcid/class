"""SqFree"""

def main(count):
    """many SqFree number"""
    total = 0
    for i in range(1, count+1):
        check = "free"
        for j in range(2, i):
            if i%(j**2) == 0:
                check = "non"
                break
            if j**2 > i:
                break
        total += 1 if check == "free" else 0
    print(total)

main(int(input()))
