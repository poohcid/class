""" OTP """
def main():
    """ OTP """
    otp = input()
    while otp != "0":
        check = list(map(lambda x: otp.count(x), set(otp)))
        if len(otp) == 4:
            print("Valid" if verified(2, 1, list(check)) else "Invalid")
        elif len(otp) == 6:
            if verified(2, 2, list(check)):
                print("Valid")
            elif verified(3, 1, list(check)):
                print("Valid")
            else:
                print("Invalid")
        elif len(otp) == 8:
            if verified(3, 2, list(check)):
                print("Valid")
            elif verified(2, 3, list(check)):
                print("Valid")
            else:
                print("Invalid")
        otp = input()

def verified(count, many, lst):
    """return verified"""
    check = 0
    for _ in range(many):
        if count in lst:
            lst.remove(count)
            check += 1
    return 1 if set(lst) == {1} and check == many else 0

main()
