start = int(input())
diff = int(input())
n = int(input())

i = start
print(i if i >= 0 else "(" + str(i) + ")", end="")

sum = i
i += diff
for _ in range(n - 1):
    print(" + {}".format(i if i >= 0 else "(" + str(i) + ")"), end="")
    sum += i
    i += diff

print(" = {}".format(sum))