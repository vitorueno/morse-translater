from ..encrypt import encrypt


def test_encrypt():
    assert encrypt('oi') == '--- .. '
    assert encrypt('OI') == '--- .. '
    assert encrypt('@') == '.--.-. '
    assert encrypt('!') == '-.-.-- '
    assert encrypt('?') == '..--.. '
    assert encrypt('$') == '...-..- '
    assert encrypt(
        '1234567890') == '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- '
    assert encrypt('\'') == '.----. '
    assert encrypt('"') == '.-..-. '
    assert encrypt('(') == '-.--. '
    assert encrypt(')') == '-.--.- '
    assert encrypt('.') == '.-.-.- '