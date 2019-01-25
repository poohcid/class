"""Perfect"""
def main(count):
    """total perfect number"""
    total = 0
    for i in range(1, count):
        if count%i == 0:
            print(i, count//i)
            total += i
    print(total)

main(int(input()))
