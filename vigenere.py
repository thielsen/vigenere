class VigenereCipher:

    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        return "Test encode"

    def extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def encode(self, plaintext):
           plaintext = plaintext.replace(" ", "").upper()
           cipher = []
           keyword = self.extend_keyword(len(plaintext))
           for p,k in zip(plaintext, keyword):
               cipher.append(combine_character(p,k))
           return "".join(cipher)    

def combine_character(plain, keyword):
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)