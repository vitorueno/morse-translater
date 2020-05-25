from ..encrypt import encrypt
from ..decrypt import decrypt

def test_encrypt_decrypt():
    assert decrypt(encrypt('OI')) == 'OI '
    assert decrypt(encrypt('PYTHON-PROGRAM')) == 'PYTHON-PROGRAM '
    mes = encrypt('oi pessoal')
    assert decrypt(mes.rstrip()) == 'OI PESSOAL'