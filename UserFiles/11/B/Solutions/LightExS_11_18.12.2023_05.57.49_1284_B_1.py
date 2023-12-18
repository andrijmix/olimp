inp = input()
out = ""

for i in inp:
    if i.isupper():
        out += chr((ord(i) - ord("A") - 3) % 26 + ord("A"))
    elif i.islower():
        out += chr((ord(i) - ord("a") - 3) % 26 + ord("a"))
    else:
        out += i
print(out)
