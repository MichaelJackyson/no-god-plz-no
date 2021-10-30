grades = list([[int(x) for x in input().split()], [int(x) for x in input().split()]])

for i in range(2):
    print("class {}".format(i + 1))
    for j in range(3):
        print(" {}: {}".format(j + 1, grades[i][j]))
    print(" sum: {}".format(sum(grades[i])))
    print(" avg: {:.2f}".format(sum(grades[i]) / len(grades[i])))

print("total: {}, avg: {:.2f}".format(sum(sum(grades, [])), sum(sum(grades, [])) / (2 * 3)))
