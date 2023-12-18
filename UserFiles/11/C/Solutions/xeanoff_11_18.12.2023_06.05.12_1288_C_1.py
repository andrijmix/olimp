from math import factorial

inp = input()
result = []

for i in inp:
    if not i in result:
        result.append(i)

print(factorial(len(result)))