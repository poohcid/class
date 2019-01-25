"""Sequence VIII"""

def main():
    """print 1 - count for count time"""
    donut_a, donut_b, = int(input()), int(input())
    donut_c, donut_d, = int(input()), int(input())
    pay = donut_a*(donut_b*(donut_d//(donut_b+donut_c)))
    total = (donut_b+donut_c)*(donut_d//(donut_b+donut_c))
    if donut_d-total >= donut_b:
        total += donut_b+donut_c
        pay += donut_a*donut_b
    else:
        pay += donut_a*(donut_d-total)
        total += donut_d%(donut_b+donut_c)
    print(pay, total)

main()
