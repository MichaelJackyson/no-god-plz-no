n = int(input())
m = int(input())
j = int(input())

print("sum is", n + m + j)
print("average is {:.2f}".format((n + m + j) / 3))
print("product is", (n * m * j))

print("smallest is {}".format(min([n, m, j])))
print("largest is {}".format(max([n, m, j])))

