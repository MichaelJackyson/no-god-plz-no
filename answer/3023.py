a = list()
b = list()

while True:
    x = int(input())
    if x == -1:
        break
    a.append(x)
    if x > 30:
        b.append(x)

print(a)
print(sorted(a))
print(sum(b))
