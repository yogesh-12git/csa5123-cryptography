def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def sdes(block):
    return block[::-1]   # simplified S-DES

def cbc_encrypt(pt, key, iv):
    blocks = [pt[i:i+8] for i in range(0, len(pt), 8)]
    ct = ""
    prev = iv
    for b in blocks:
        temp = xor(b, prev)
        enc = sdes(temp)
        ct += enc
        prev = enc
    return ct

def cbc_decrypt(ct, key, iv):
    blocks = [ct[i:i+8] for i in range(0, len(ct), 8)]
    pt = ""
    prev = iv
    for b in blocks:
        temp = sdes(b)
        pt += xor(temp, prev)
        prev = b
    return pt

pt = "0000000100100011"
key = "0111111101"
iv = "10101010"

ct = cbc_encrypt(pt, key, iv)
print("Ciphertext:", ct)
print("Decrypted :", cbc_decrypt(ct, key, iv))
