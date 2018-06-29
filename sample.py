import random
import hashlib

print("Hello, Python-Bitcoin World!")
print(list(range(8)))
for i in range(0, 256):
    v = random.randrange(256)
    s = '{idx}: {random1} {random2} {random3}'.format(idx=i,
                                                      random1=format(v, 'x'),
                                                      random2=format(v, '02x'),
                                                      random3=format(v, '#04x'))
    print(s)
print()

print(hashlib.sha256(b"Elen sila lumen omentielvo!").hexdigest())
print()

encodedBytes = bytes("これは日本語です。".encode("utf-8"))
print(encodedBytes.hex())

hexString = ""
for i in range(len(encodedBytes)):
    s = format(encodedBytes[i], '02x')
    print(s, end=' ')
    hexString = hexString + s

print()
print(hexString)
parsedBytes = bytes.fromhex(hexString)
rebuiltString = parsedBytes.decode("utf-8")
print(rebuiltString)
print()