import pycoin.key.BIP32Node
import pycoin.encoding


def print_node(n, path):
    print('pubkey (hwif) for {node}: {pubkey}'.format(node=path, pubkey=n.hwif(as_private=False)))
    if n.secret_exponent() is not None:
        print('privkey (hwif) for {node}: {prvkey}'.format(node=path, prvkey=n.hwif(as_private=True)))
    else:
        print('privkey for {node}: None'.format(node=path))


seed = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
master_node1 = pycoin.key.BIP32Node.BIP32Node.from_master_secret(seed)
print_node(master_node1, 'm')

s1 = master_node1.subkey_for_path('0H')
print_node(s1, '0H')

s2 = master_node1.subkey_for_path('0H/1/2H/2/1000000000')
print_node(s2, '0H/1/2H/2/1000000000')

s3 = master_node1.subkey_for_path('0/1/2')
print_node(s3, '0/1/2')

print()

master_node2 = pycoin.key.BIP32Node.BIP32Node.from_hwif("xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8")
print_node(master_node2, 'm')
s3_2 = master_node2.subkey_for_path('0/1/2')
print_node(s3_2, '0/1/2')
