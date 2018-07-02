import random
import pycoin.key.BIP32Node
import pycoin.encoding

import hashlib


def generate_pseudo_random_bytes(num_bytes):
    return bytes(random.getrandbits(8) for _ in range(num_bytes))


for _ in range(1):
    master_secret = generate_pseudo_random_bytes(32)
    print('master secret (hex): {master_secret}'.format(master_secret=master_secret.hex()))
    print()

    node = pycoin.key.BIP32Node.BIP32Node.from_master_secret(master_secret)
    print('private key (int): {pk_hex}'.format(pk_hex=node.secret_exponent()))
    print('private key (wif): {pk_wif}'.format(pk_wif=node.wif()))
    print('address: {address}'.format(address=node.address()))
    print()

    secret_exponent = node.secret_exponent()
    wif_not_compressing = pycoin.encoding.secret_exponent_to_wif(secret_exponent, compressed=False)
    wif_compressing = pycoin.encoding.secret_exponent_to_wif(secret_exponent, compressed=True)
    print('private key (wif, not compressing, calculated): {pk}'.format(pk=wif_not_compressing))
    print(pycoin.encoding.wif_to_tuple_of_secret_exponent_compressed(wif_not_compressing))
    print('private key (wif, compressing, calculated): {pk}'.format(pk=wif_compressing))
    print(pycoin.encoding.wif_to_tuple_of_secret_exponent_compressed(wif_compressing))
    print()

    public_key_pair = node.public_pair()
    print('public key (int pair): {pubkey_int_pair}'.format(pubkey_int_pair=public_key_pair))
    print('public key (hex pair): ({pubkey_x}, {pubkey_y})'.format(
        pubkey_x=public_key_pair[0].to_bytes(32, 'big').hex(),
        pubkey_y=public_key_pair[1].to_bytes(32, 'big').hex()))
    sec_bytes = pycoin.encoding.public_pair_to_sec(public_key_pair, compressed=True)
    # print('public key (sec): {pubkey_hex}'.format(pubkey_hex=sec_bytes))
    print('public key (compressed sec hex): {pubkey_hex}'.format(pubkey_hex=sec_bytes.hex()))
    digest1 = hashlib.sha256(sec_bytes)
    print('digest1 (SHA256): {digest1}'.format(digest1=digest1.hexdigest()))
    digest2 = pycoin.encoding.ripemd160(digest1.digest())
    print('digest2 (RIPEMD160): {digest2}'.format(digest2=digest2.hexdigest()))
    address = pycoin.encoding.hash160_sec_to_bitcoin_address(digest2.digest())
    print('address (calculated): {address}'.format(address=address))
    print()
    print(node)




