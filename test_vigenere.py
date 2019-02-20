from vigenere import *

def test_encode():
      cipher = VigenereCipher("DONKEY")
      encoded = cipher.encode("TESTENCODING")
      assert encoded == "Test encode"