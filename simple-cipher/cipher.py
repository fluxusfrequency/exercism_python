class Caesar:
    def encode(self, input):
        print(ord('z'))
        return "".join([self.__encode_letter(letter) for letter in input])

    def __encode_letter(self, letter):
        code = ord(letter)
        if code >= 122:
            code -= 26
        return chr(code + 3)

def Cipher(stuff):
    return True
