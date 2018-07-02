import random
import generate_address_pycoin
import generate_address_pybitcointools


def generate_pseudo_random_bytes(num_bytes):
    return bytes(random.getrandbits(8) for _ in range(num_bytes))


# master_secret = bytes.fromhex('4d783845129ddbf88506e9294fec1dffb6a0d6462f363ace88ee545aa19e710f')
master_secret = generate_pseudo_random_bytes(32)
print('master secret (hex): {master_secret}'.format(master_secret=master_secret.hex()))
print()

print("=======pyboin=======")
node = generate_address_pycoin.generate_node(master_secret)
print()

print("=======pybitcointools=======")
secret_int = node.secret_exponent()
secret_bytes = secret_int.to_bytes(32, 'big')
address = generate_address_pybitcointools.generate_address(secret_bytes)
print()

print(node.address() == address)





