input_path = input()
with open(input_path, "r") as f:
    n1 = int(f.read())

n2 = int(input())

with open("wr01.txt", "w") as f:
    f.write(" ".join([
        str(i) for i in range(1, (n1 + n2 + 1)) 
    ]) + " ")