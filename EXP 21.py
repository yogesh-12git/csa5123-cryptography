BLOCK_SIZE = 8

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def pad(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([0x80]) + bytes([0x00] * (pad_len - 1))

key = b"mysecret"
iv = b"initvect"
plaintext = b"This is a test of ECB, CBC, and CFB modes."

padded = pad(plaintext)

# ECB
ecb = b""
for i in range(0, len(padded), BLOCK_SIZE):
    ecb += xor_bytes(padded[i:i+8], key)

# CBC
cbc = b""
prev = iv
for i in range(0, len(padded), BLOCK_SIZE):
    block = xor_bytes(padded[i:i+8], prev)
    enc = xor_bytes(block, key)
    cbc += enc
    prev = enc

# CFB
cfb = b""
prev = iv
for i in range(0, len(padded), BLOCK_SIZE):
    temp = xor_bytes(prev, key)
    enc = xor_bytes(temp, padded[i:i+8])
    cfb += enc
    prev = enc

print("ECB :", ecb.hex())
print("CBC :", cbc.hex())
print("CFB :", cfb.hex())
