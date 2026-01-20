def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

e = 31
n = 3599

# trial-and-error factorization
for i in range(2, n):
    if n % i == 0:
        p = i
        q = n // i
        break

phi = (p - 1) * (q - 1)
_, d, _ = egcd(e, phi)
d = d % phi

print("p =", p)
print("q =", q)
print("Private key d =", d)
