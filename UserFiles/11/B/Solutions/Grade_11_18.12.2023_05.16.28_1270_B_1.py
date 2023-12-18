import string


s = input()
res = []
literals_lower = string.ascii_lowercase
literals_upper = string.ascii_uppercase
for i in s:
    if i.islower():
        res += [literals_lower[literals_lower.index(i) - 3]]
    elif i.isupper():
        res += [literals_upper[literals_upper.index(i) - 3]]
print("".join(res))