n = int(input())
m = int(input())
j = int(input())
print("sum is", n+m+j) 
print("average is {:.2f}".format((n+m+j)/3))
print("product is", (n*m*j))
if n < j and n < m:
    print("smallest is", n)
if m < j and m < n:
     print("smallest is", m)
if j < n and j < m:
     print("smallest is", j)  
if n > j and n > m:
    print("largest is", n)
if m > j and m > n:
     print("largest is", m)
if j > n and j > m:
     print("largest is", j)  
