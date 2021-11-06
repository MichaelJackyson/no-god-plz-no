n = int(input())

mod_equals_0 = 0
mod_equals_1 = 0
mod_equals_2 = 0

for i in range(n):
    num = int(input())
    
    if num % 3 == 0:
        mod_equals_0 += 1
    elif num % 3 == 1:
        mod_equals_1 += 1
    else:
        mod_equals_2 += 1

print(mod_equals_0, mod_equals_1, mod_equals_2)
