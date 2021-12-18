arr = list()

while True:
    try:
        buf = int(input())
        arr.append(buf)
    except ValueError:
        break

ans = 0
for i, j in zip(arr[:-1], arr[1:]):
    if i == 1 and j == 9:
        ans += 1

print(ans)