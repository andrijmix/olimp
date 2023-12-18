a, b = int(input()), input()
for i in range(a):
    print(b, end="")
    if i != a - 1:
        print(" ", end="")
