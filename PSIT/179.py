"""BloodDonation"""

def main():
    """BloodDonation"""
    age = int(input())
    weight = int(input())
    count = int(input())
    result = "Yes"
    if not 17 <= age <= 70:
        result = "No"
    elif weight < 45:
        result = "No"
    elif count == 0 and age > 55:
        result = "No"
    if age == 17 or 60 <= age <= 70:
        ver = input()
        if ver == "False":
            result = "No"
    print(result)

main()
