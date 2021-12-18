import numpy as np


head_num, foot_num = list([int(x) for x in input().split()])

ans = np.linalg.solve([[1, 1], [2, 4]], [head_num, foot_num])

if round(ans[0]) == ans[0] and round(ans[1]) == ans[1]:
    print("YES\n{} {}".format(int(ans[0]), int(ans[1])))
else:
    print("NO")