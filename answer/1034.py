my_list = list()

for i in range(5):
    my_list.append(int(input()))

for i in range(5):
    print("{}\t{}".format(my_list[i], "*" * my_list[i]))

