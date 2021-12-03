def P(n, m):
    def factorial(n):
            f = 1
            for i in range(1, n + 1):
                f *= i
            return f
    return factorial(n) / (factorial(m) * factorial(n - m))


print(int(P(int(input()), int(input()))))
