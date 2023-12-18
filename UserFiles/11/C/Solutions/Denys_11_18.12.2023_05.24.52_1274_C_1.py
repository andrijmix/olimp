from itertools import permutations
s = input()
rez = len(set(permutations(s)))
print(rez)
