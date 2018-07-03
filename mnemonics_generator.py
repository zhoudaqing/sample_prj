import bitcoin
import hashlib
import hmac
import unicodedata
import pbkdf2


def normalize_string(txt):
    return unicodedata.normalize('NFKD', txt)


def to_seed(mnemonic_phrase, passphrase=''):
    mn = normalize_string(mnemonic_phrase)
    p = normalize_string(passphrase)
    return pbkdf2.PBKDF2(mn, u'mnemonic' + p, iterations=2048, macmodule=hmac,
                                 digestmodule=hashlib.sha512).read(64)


words = bitcoin.entropy_to_words(bytes.fromhex('00000000000000000000000000000000'))
print(words)
mnemonics = ' '.join(words)
print(">" + mnemonics + "<")

seed = to_seed(mnemonics, "TREZOR")
print(seed.hex())
