import math

n = 3599
known_plaintext = 122   # shares factor with n

factor = math.gcd(known_plaintext, n)

if factor != 1 and factor != n:
    print("Found factor:", factor)
    print("Other factor:", n // factor)
else:
    print("No useful factor found")
