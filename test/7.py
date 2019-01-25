""" FibonacciRecursionV2 """
def fibo(num, fbd):
    """ dict of fibonucci """
    tmp = fbd
    keys = num//2
    keys_od = keys + (num%2 == 1)
    keys_ev = keys - (num%2 == 0)
    if num not in (0, 1, 2):
        if keys_ev not in tmp:
            tmp.update(fibo(keys_ev, tmp))
        if keys_od not in tmp:
            tmp.update(fibo(keys_od, tmp))
        if keys+1 not in tmp:
            tmp.update(fibo(keys + 1, tmp))
        tmp.update({num:tmp[keys+1]*tmp[keys_od] + tmp[keys]*tmp[keys_ev]})
    return tmp


def main(num):
    """ main func """
    # fibo_dict = {key=n:value=f(n)}
    # f0 = f2*f0+f0*f-1: Can't use
    # f1 = f1*f1+f0*f0
    # f2 = f2*f1+f1*f0
    # ex: f16 -> 9*8+8*7 -> (5*5+4*4)*(5*4+4*3)+(5*4+4*3)*(4*4+3*3)
    fbd = {0:0, 1:1, 2:1}
    print(fibo(num, fbd)[num])


main(int(input()))
