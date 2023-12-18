import math


def perm(string):
    if not (string.isupper() or string.islower()):
        return 0
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1

    total_permutations = math.factorial(len(string))
    for count in char_counts.values():
        total_permutations //= math.factorial(count)
    return total_permutations


inp = input()
print(perm(inp))
