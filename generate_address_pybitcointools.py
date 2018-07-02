import bitcoin


def generate_address(secret_bytes):
    int_privkey = int.from_bytes(secret_bytes, 'big')
    print('privkey (int): {privkey}'.format(privkey=int_privkey))
    wif_not_compressing_privkey = bitcoin.encode_privkey(secret_bytes, 'wif')
    print('privkey (wif, not compressing): {privkey}'.format(privkey=wif_not_compressing_privkey))
    wif_compressing_privkey = bitcoin.encode_privkey(secret_bytes, 'wif_compressed')
    print('privkey (wif, compressing): {privkey}'.format(privkey=wif_compressing_privkey))
    print()

    public_key = bitcoin.fast_multiply(bitcoin.G, int_privkey)
    print('pubkey pair (int): {pubkey}'.format(pubkey=public_key))
    pubkey_not_compressed = bitcoin.encode_pubkey(public_key, 'hex')
    print('pubkey (not compressed, hex): {pubkey}'.format(pubkey=pubkey_not_compressed))
    pubkey_compressed = bitcoin.encode_pubkey(public_key, 'hex_compressed')
    print('pubkey (compressed, hex): {pubkey}'.format(pubkey=pubkey_compressed))
    address_not_compressed = bitcoin.pubkey_to_address(public_key)
    print('address (not compressed, b58check): {address}'.format(address=address_not_compressed))
    address_compressed = bitcoin.pubkey_to_address(pubkey_compressed)
    print('address (compressed, b58check): {address}'.format(address=address_compressed))
    return address_compressed


