result = [num for num in list(map(int, input("").split())) if num % 7 == 0 and num % 5 != 0]
print(' '.join(map(str, result)))
