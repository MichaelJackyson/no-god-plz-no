a = int(input())
b = int(input())
c = int(input())

if a + b > c:
    print(1)
elif a + c > b:
    print(1)
elif b + c > a:
    print(1)
else:
    print(0)