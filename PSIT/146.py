"""password"""
import hashlib

def main():
    """password"""
    text = input()
    b_text = text.encode()
    print(hashlib.sha512(b_text).hexdigest().upper())

main()
