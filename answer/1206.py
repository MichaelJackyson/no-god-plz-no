file_name = input()
with open(file_name, "r") as f:
    buf = f.read()

print(buf, end="")

# print(open(input(), "r").read(), end="")