def calcualate_BMI(weight, height):
    bmi = round(int(weight) / (int(height) / 100 * int(height) / 100), 2)
    if bmi < 16:
        return ("Your BMI is {0}. You are severely underweight.".format(bmi))
    elif bmi <= 18.5:
        return ("Your BMI is {0}. You are underweight.".format(bmi))
    elif bmi <= 25:
        return ("Your BMI is {0}. You are normal.".format(bmi))
    elif bmi <= 30:
        return ("Your BMI is {0}. You are overweight.".format(bmi))
    elif bmi > 30: 
        return ("Your BMI is {0}. You are obese.".format(bmi))  