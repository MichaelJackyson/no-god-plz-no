n = int(input())

for i, j in zip(range(n - 1, -1, -1), range(1, 2 * n, 2)):
    print(" " * i + "*" * j)
