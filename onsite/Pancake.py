"""Pancake"""

def main(cake_a, cake_b, cake_c):
    """Function_input_"""
    total, price, count = 0, 0, cake_c
    while total < cake_c:
        if count < cake_a:
            price += (cake_c-total)
            total += (cake_c-total)
        elif cake_a <= cake_c:
            count -= (cake_a+cake_b)
            price += cake_a
            total += cake_a+cake_b
        else:
            price, total = cake_c, cake_c
    print("Pay: %d" %(price*20))
    print("Get: %d" %total)

main(int(input()), int(input()), int(input()))
