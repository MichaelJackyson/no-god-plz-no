n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        ans = (i + 1) * (j + 1)
        print("{}*{}={}".format((i + 1), (j + 1), " " + str(ans) if ans < 10 else ans), end=" ")
    print("")
