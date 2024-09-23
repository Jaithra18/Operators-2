
weight=float(input("Enter your weight in KG"))
height=float(input("Enter your height im CM"))
BMI=weight/(height/100)**2
print("Your BMI is",round(BMI,2))
if BMI<=18.4:
    print("you are underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
elif BMI<=34.9:
    print("you are obese")
else:
    print("you are extremely obese")