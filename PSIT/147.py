"""password"""
import hashlib

def main():
    """password"""
    code = input()
    for i in range(100000):
        number = "%05d" %i
        b_num = number.encode()
        b_num = hashlib.sha512(b_num).hexdigest().upper()
        if b_num == code:
            print(number)
            break

main()
