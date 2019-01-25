"""Inverter"""

def main():
    """Inverter"""
    bits = input()
    debits = ""
    for i in bits:
        debits += str(int(i == "0"))
    print(debits.lstrip("0"))

main()
