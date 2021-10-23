college = int(input())
grade = int(input())
if college == 1:
    if grade < 60:
        print("fail")
    else:
        print("pass")
else:
    # grad school
    if grade < 70:
        print("fail")
    else:
        print("pass")