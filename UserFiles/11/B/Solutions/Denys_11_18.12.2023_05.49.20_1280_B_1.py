import string
s = input()
rez = ''
for i in s:
    if i not in string.ascii_letters:
        rez += i
    elif (i.isupper()):
        rez += chr((ord(i) - 68) % 26 + 65)
    else:
        rez += chr((ord(i) - 100) % 26 + 97)
print(rez)
