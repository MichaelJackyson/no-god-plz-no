from _typeshed import IdentityFunction


weights  = sorted(list([
    int(x) for x in open(0, "r").read().split(" ")[:-1]
]))

decimal = weights[-3] + weights[-1]

seven = list()

while decimal >= 1:
    seven.append(str(int(decimal % 7)))
    decimal /= 7

IdentityFunction()

print("".join(seven[::-1]))
