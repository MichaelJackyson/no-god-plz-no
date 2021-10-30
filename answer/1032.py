numbers = list([int(x) for x in open(0).read().split()])

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            buf = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = buf

print(" ".join(list([str(x) for x in numbers])), end=" \n")
