from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    list_posts = [
        {
            "title": "Try me",
            "content": "Try me",
            "author": "The Weeknd",
            "gender": 0
        },
        {
            "title": "Wasted time",
            "content": "Wasted time",
            "author": "The Weeknd",
            "gender": 1
        }
    ]
    return render_template("index.html", list_posts = list_posts)

@app.route("/say-hello/name")
def my_name():
    return "Hi. My name is Phong."

@app.route("/hello")
def hello():
    return "Hello C4E 19"

@app.route("/say-hi/<name>/<age>")
def say_hi(name, age):
    return ("Hi. My name is {0}. I'm {1} years old.".format(name, age))

@app.route("/sum/<int:number_1>/<int:number_2>")
def sum(number_1, number_2):
    # sum = int(number_1) + int(number_2)
    # return ("Result: {0}".format(int(number_1) + int(number_2)))
    return ("Result: ") + str(number_1 + number_2)

if __name__ == '__main__':
  app.run(debug = True)
