from flask import Flask, render_template
serious_exercies_1 = Flask(__name__)

@serious_exercies_1.route('/')
def index():
    return ("Serious Exercies 1")

@serious_exercies_1.route("/bmi/<int:weight>/<int:height>")
def calcualate_BMI(weight, height):
    # (int(weight) / (int(height) / 100 * int(height) / 100)
    return render_template("bmi.html", weight = weight, height = height)
    
if __name__ == '__main__':
  serious_exercies_1.run(debug=True)
    

    