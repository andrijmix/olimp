inp = map(int, input().split())
ans = []
for i in inp:
    if i % 7 == 0 and i % 5 != 0:
        ans.append(str(i))
print(" ".join(ans))
