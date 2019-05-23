""" """

def main():
    money = int(input())*12
    diff = 0
    if money >= 5000001:
        diff += money*0.35
    if money >= 2000001:
        diff += mni(money, 5000000)*0.30
    if money >= 1000001:
        diff += mni(money, 2000000)*0.25
    if money >= 750001:
        diff += mni(money, 1000000)*0.20
    if money >= 500001:
        diff += mni(money, 750000)*0.15
    if money >= 300001:
        diff += mni(money, 500000)*0.10
    if money >= 150001:
        diff += mni(money, 300000)*0.05
    result = float((money - diff)/12)
    print("%.2f" %result)

def mni(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

main()