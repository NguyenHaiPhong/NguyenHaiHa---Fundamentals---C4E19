your_height_in_cm = int(input("Enter your height (cm): "))
your_weight = int(input("Enter your height (kg): "))
your_height_in_m = your_height_in_cm / 100 
bmi = round(your_weight / (your_height_in_m * your_height_in_m), 2)
# print("Your BMI (Body Mass Index) = mass (kg) / (height(m) x height(m)) =", your_weight, "/", print("("), your_height_in_m, print("x"), your_height_in_m, print(") ="), bmi)
print("Your BMI (Body Mass Index) =", bmi)
if bmi < 16:
    print("You are severely underweight.")
elif bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 25:
    print("You are normal.")
elif bmi <= 30:
    print("You are overweight.")
else: 
    print("You are obese.")