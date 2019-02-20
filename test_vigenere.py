from vigenere import *

def test_encode():
      cipher = VigenereCipher("DONKEY")
      encoded = cipher.encode("TESTENCODING")
      assert encoded == "Test encode"

def test_encode_character():
      cipher = VigenereCipher("DONKEY")
      encoded = cipher.encode("E")
      assert encoded == "X"

def test_encode_spaces():
      cipher = VigenereCipher("DONKEY")
      encoded = cipher.encode("TEST ENCODING")
      assert encoded == "Test encode"

def test_encode_mixedcase():
      cipher = VigenereCipher("DONkey")
      encoded = cipher.encode("Test ENCOding")
      assert encoded == "Test encode"

def test_combine_character():
      assert combine_character("F", "T") == "Y"
      assert combine_character("O", "R") == "F"