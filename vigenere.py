class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword
    def encode(self, plaintext):
        return "Test encode"

def combine_character(plain, keyword):
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)