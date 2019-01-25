"""Perfect"""
def main(count):
    """total perfect number"""
    print(1)
    print(2)
    check, total = 2, 3
    for i in range(3, count//2 + 1):
        if count%i == 0:
            print("%d %d %d" %(i, 2**check, 2**check - i))
            total += i
            check += 1
    print(total)

main(int(input()))
