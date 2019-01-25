"""Restaurant"""

def main():
    """function"""
    pay = float(input())
    service = float((pay*0.1))
    vat = float((pay*0.07))
    total = pay+service+vat
    print("Service Charge : %.2f Baht" %service)
    print("VAT : %.2f Baht" %vat)
    print("Total : %.2f Baht" %total)
main()
