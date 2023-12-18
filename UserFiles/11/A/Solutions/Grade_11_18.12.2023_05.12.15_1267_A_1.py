numbers = list(range(1, 101))
print(" ".join([str(i) for i in numbers if i % 5 != 0 and i % 7 == 0]))
