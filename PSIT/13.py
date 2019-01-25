"""Additive"""

def main():
    """Function process and print"""
    import math
    num1, num2 = math.radians(90), math.radians(60)
    num3, num4 = math.radians(245**2), math.radians(180)
    print((math.sin(num1) + math.sin(num2)**2)/\
        (math.cos(num3) + math.cos(num4)))
    print((math.factorial(16)*math.factorial(4))/math.factorial(8))
    print(40/math.sqrt((25-12)**2 + (12-15)**2))
    print(math.log(1234**4, 10))
    print((math.log(4234, 5) + math.log(8191, 2) + 71*math.log(156154, 10))/\
        (math.log(777, 7) - math.log(888, 8) - math.log(999, 9)))

main()
