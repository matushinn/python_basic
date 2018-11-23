#A11
height = float(input("Height(m)?> "))

weight = float(input("Weight(kg)?> "))

bmi = round(weight / (height * height), 2)


print(f"Your BMI is {bmi}")
