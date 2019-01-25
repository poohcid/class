"""Amicable"""

def main():
    """Amicable"""
    count = int(input())
    lst_ami = [0]
    if count < 220:
        return [0]
    for i in range(220, count+1):
        num1 = sum(divisor(i))
        num2 = sum(divisor(num1))
        if num2 == i and i != num1:
            lst_ami.append(i)
    return lst_ami

def divisor(number):
    """return list divisor number"""
    lst_divi = [1]
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            lst_divi += [i, number//i]
    return lst_divi

print(sum(main()))
