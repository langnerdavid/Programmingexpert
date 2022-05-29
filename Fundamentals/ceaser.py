def caesar_cipher(string, offset):
    caesar = ""
    for char in string:
        if (ord(char) - offset) >= ord("a"):
            caesar += chr(ord(char) - offset)
        else:
            caesar += chr(ord(char) + 27 - offset)
    return caesar

print(caesar_cipher("abc", 20))