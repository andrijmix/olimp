n, m = map(int, input("Рядок/Стовбець: ").split())


matrix = [list(map(int, input().split())) for _ in range(n)]
matrix = [list(row) for row in zip(*matrix)]

for row in matrix:
    print(*row)
