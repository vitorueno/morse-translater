from ..encrypt import encrypt
from morse.decrypt import decrypt

def test_encrypt_decrypt():
    assert decrypt(encrypt('OI')) == 'OI '
    assert decrypt(encrypt('PYTHON-PROGRAM')) == 'PYTHON-PROGRAM '