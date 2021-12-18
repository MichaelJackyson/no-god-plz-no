height = int(input())
weight = int(input())

bmi = weight / (height / 100.0) ** 2

print("{:.2f}".format(bmi))

if bmi < 18.5:
    print("Underweight")
elif bmi < 24:
    print("Normal")
elif bmi < 27:
    print("Overweight")
elif bmi < 30:
    print("Obese Class I")
elif bmi < 35:
    print("Obese Class II")
else:
    print("Obese Class III")