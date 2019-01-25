"""ProgressiveTax"""
def check(num, total):
    """fuction"""
    count = 0
    dic = {"4000000":0.35, "2000000":0.3, "1000000":0.25, \
    "750000":0.2, "500000":0.15, "300000":0.1, "150000":0.05}
    for i in dic:
        if num > int(list(i)[0]) and count == 0:
            total += (num-int(list(i)[0]))*int(i)
            count += 1
            old = int(list(i)[0])
        if num > int(list(i)[0]) and count != 0:
            total += (old-int(list(i)[0]))*int(i)
            old = int(list(i)[0])
    print(int(total))
check(int(input()), 0)
