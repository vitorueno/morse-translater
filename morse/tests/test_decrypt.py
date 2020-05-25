from ..decrypt import decrypt

def test_decrypt():
    assert decrypt('- . ... - .') == 'TESTE'
    assert decrypt('-.-.-- ...-..-') == '!$'
    assert decrypt(
        '--- .. --..--  -.-. --- -- ---  ...- .- ..  ...- --- -.-. .') == 'oi, como vai voce'.upper()
    assert decrypt('--- ..  .--. . ... ... --- .- .-..') == 'OI PESSOAL'