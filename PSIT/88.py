"""Kaprekar's Constant"""

def main(num, count):
    """condition statement"""
    while num != "6174":
        count += 1
        high, loww = high_and_low(num)
        num = "%04d" %(int(high)-int(loww))
    print(count)

def high_and_low(num):
    """return highest and lower"""
    num1, num2, num3, num4 = num[0], num[1], num[2], num[3]
    num1, num2 = stack(num1, num2)
    num1, num3 = stack(num1, num3)
    num1, num4 = stack(num1, num4)
    num2, num3 = stack(num2, num3)
    num2, num4 = stack(num2, num4)
    num3, num4 = stack(num3, num4)
    return num1+num2+num3+num4, num4+num3+num2+num1

def stack(num1, num2):
    """return high and low"""
    if int(num1) > int(num2):
        return num1, num2
    else:
        return num2, num1

main(input(), 0)
