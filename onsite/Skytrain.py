"""Skytrain"""

def main():
    """Function_input_"""
    coin = int(input())
    if coin >= 4:
        print("Mo Chit (N8)\nSaphan Khwai (N7)")
    if coin >= 6:
        print("Ari (N5)\nSanam Pao (N4)")
    if coin >= 7:
        print("Victory Monument (N3)")
    if coin >= 8:
        print("Phaya Thai (N2)\nRatchathewi (N1)")
    if coin >= 9:
        print("Siam (CEN)")

main()
