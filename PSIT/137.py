"""CircularPrime"""

def main(count):
    """CircularPrime"""
    total = [2*(count >= 2)]
    for i in range(3, count+1, 2):
        if i not in total:
            number = slot_n(str(i))
            if 0 not in number:
                total += number
            total = list(set(total))
            total.sort(key=int)
    result = list(filter(lambda x: int(x) <= count, total))
    #print(result)
    print(list(map(int, result)))

def slot_n(num):
    """slot"""
    result = [str(int(num)*(isprime(int(num)))), num]
    for i in num:
        num1 = result[-1][1:] + i
        if isprime(int(num1)) and int(num1)%2 != 0:
            result.append(num1)
        else:
            result = [0]
            break
    return list(set(result))

def isprime(number):
    """prime to true"""
    check = 1
    for i in range(3, int(number**0.5)+1, 2):
        if number%i == 0:
            check = 0
            break
    return check

main(int(input()))
