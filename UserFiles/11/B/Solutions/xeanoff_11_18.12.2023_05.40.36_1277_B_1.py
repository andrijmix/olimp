inp = input()
result = ''
    
for char in inp:
    if char.isalpha():
        decrypted_char = chr((ord(char) - 3 - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) - 3 - ord('a')) % 26 + ord('a'))
        result += decrypted_char
    else:
        result += char
    
print(result)

