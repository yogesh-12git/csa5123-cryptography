def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def sdes(block):
    # Simplified S-DES encryption (reverse bits)
    return block[::-1]

def increment(counter):
    return format(int(counter, 2) + 1, '08b')

def ctr_encrypt(pt, counter):
    blocks = [pt[i:i+8] for i in range(0, len(pt), 8)]
    ct = ""
    ctr = counter
    for b in blocks:
        keystream = sdes(ctr)
        ct += xor(b, keystream)
        ctr = increment(ctr)
    return ct


# ===== INPUT (as per word file) =====
plaintext = "000000010000001000000100"
counter = "00000000"

cipher = ctr_encrypt(plaintext, counter)

print("Ciphertext:", cipher)
print("Decrypted :", ctr_encrypt(cipher, counter))
