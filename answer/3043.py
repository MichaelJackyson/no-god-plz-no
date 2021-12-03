a = [int(x) for x in input().split()[1:-1]]

a.insert(0, 0)
a.append(0)

ans = 0
for i in range(len(a) - 1):
    if a[i + 1] > a[i]:
        ans += (a[i + 1] - a[i]) * 10
    elif a[i + 1] < a[i]:
        ans += (a[i] - a[i + 1]) * 6
    else:
        ans += 5

print(ans)
