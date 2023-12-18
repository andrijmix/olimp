def decrypt_caesar_cipher(text):
    decrypted_text = "".join(chr(((ord(char) - 3 - (ord('a') if char.islower() else ord('A'))) % 26) + (ord('a') if char.islower() else ord('A'))) if char.isalpha() else char for char in text)
    return decrypted_text

encrypted_text = input("")
print(decrypt_caesar_cipher(encrypted_text))
