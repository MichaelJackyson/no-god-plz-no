start, end = list([int(x) for x in input().split()])


def is_armstrong(number):
    if number == sum(list([int(x) ** len(str(number)) for x in str(number)])):
        return True
    return False


ans_arr = list()
for i in range(start, end + 1):
    if is_armstrong(i):
        ans_arr.append(str(i))

if ans_arr:
    print(" & ".join(ans_arr))
else:
    print("none")