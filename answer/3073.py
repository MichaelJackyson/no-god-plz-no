def return2num(n=0):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return (fac, sum([i for i in range(1, n + 1)]))

a, b = return2num(int(input()))
print("{}\n{}".format(a, b))
