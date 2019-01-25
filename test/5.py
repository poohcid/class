"""Perfect"""
def main(count):
    """total perfect number"""
    for i in range(6, count+1):
        check = 1
        for j in range(2, 16):
            if i%(2**j) != 0:
                check = 0
                break
        if check == 1:
            print(i)

main(int(input()))
