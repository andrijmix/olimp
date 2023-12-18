inp = [int(x) for x in input().split()]

result = ""
for x in inp:
    if x % 7 == 0 and x % 5 != 0:
        result += str(x) + " "

print(result[:-1:])