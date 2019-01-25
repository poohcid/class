"""All_Primes"""

def main():
    """All_Primes"""
    count = int(input())
    total = 1*(count >= 2)
    for i in range(3, count+1, 2):
        for j in range(3, i+1, 1):
            if i%j == 0:
                divi = j
                break
        if i == divi:
            total += 1
    print(total)

main()
