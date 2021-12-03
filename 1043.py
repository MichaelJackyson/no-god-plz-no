a = input()
b = input()


if (len(a))<(len(b)):
    print("1<2")
elif  (len(a))>(len(b)):
    print("1>2")
else:
    if a > b:
        print("1>2")
    elif a < b:
        print("1<2")
    else:
        print("1==2")  

print(a+b)
print(len(a+b))