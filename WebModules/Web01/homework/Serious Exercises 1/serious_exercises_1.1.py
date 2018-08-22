from flask import Flask
serious_exercies_1 = Flask(__name__)


@serious_exercies_1.route('/')
def index():
    return ("Serious Exercies 1")

@serious_exercies_1.route("/bmi/<weight>/<height>")
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
    
if __name__ == '__main__':
  serious_exercies_1.run(debug=True)
 