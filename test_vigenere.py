from app.vigenere import VigenereCipher
from app.vigenere import combine_character
from app.vigenere import separate_character


def test_encode():
    cipher = VigenereCipher("DONKEY")
    encoded = cipher.encode("TESTENCODING")
    assert encoded == "WSFDILFCQSRE"

def test_encode_character():
    cipher = VigenereCipher("DONKEY")
    encoded = cipher.encode("E")
    assert encoded == "H"

def test_encode_spaces():
    cipher = VigenereCipher("DONKEY")
    encoded = cipher.encode("TEST ENCODING")
    assert encoded == "WSFDILFCQSRE"

def test_encode_mixedcase():
    cipher = VigenereCipher("DONkey")
    encoded = cipher.encode("Test ENCOding")
    assert encoded == "WSFDILFCQSRE"

def test_combine_character():
    assert combine_character("F", "T") == "Y"
    assert combine_character("O", "R") == "F"

def test_extend_keyword():
    cipher = VigenereCipher("DONKEY")
    extended = cipher.extend_keyword(20)
    assert extended == "DONKEYDONKEYDONKEYDO"

def test_decode_separate_character():
    assert separate_character("Y", "T") == "F"
    assert separate_character("F", "R") == "O"

def test_decode():
    cipher = VigenereCipher("DONKEY")
    decoded = cipher.decode("WSFDILFCQSRE")
    assert decoded == "TESTENCODING"
    