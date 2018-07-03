import bitcoin
import hashlib
import hmac
import unicodedata
import pbkdf2


def normalize_string(txt):
    return unicodedata.normalize('NFKD', txt)


def to_seed(mnemonic, passphrase=''):
    mn = normalize_string(mnemonics)
    p = normalize_string(passphrase)
    return pbkdf2.PBKDF2(mn, u'mnemonic' + p, iterations=2048, macmodule=hmac,
                                 digestmodule=hashlib.sha512).read(64)


words = bitcoin.entropy_to_words(bytes.fromhex('066dca1a2bb7e8a1db2832148ce9933eea0f3ac9548d793112d9a95c9407efad'))
print(words)
mnemonics = ' '.join(words)
print(">" + mnemonics + "<")

entropy1 = to_seed(mnemonics, "TREZOR")
print(entropy1.hex())
