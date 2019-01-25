"""Perfect"""
def main(count):
    """total perfect number"""
    prime = [2, 3, 5, 7, 13, 17, 19, 31] #limit list
    total = []
    for i in prime:
        num = (2**i - 1)*(2**(i-1))
        total.append(num)
        if total[-1] > count:
            del total[-1]
            break
    print(0 if count < 6 else sum(total))

main(int(input()))
