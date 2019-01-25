"""Milk"""

def main(num_a, num_b, num_c, num_d):
    """statement"""
    fhaa, milk = num_d//num_a, 0
    while (fhaa >= num_b) and (num_b != 0):
        milk += num_b*(fhaa//num_b)
        fhaa = num_c*(fhaa//num_b) + fhaa%num_b
    print(fhaa+milk)

main(int(input()), int(input()), int(input()), int(input()))
