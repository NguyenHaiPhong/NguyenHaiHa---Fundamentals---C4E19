from flask import Flask, render_template, redirect
exercies_1 = Flask(__name__)


@exercies_1.route('/')
def index():
    return "Exercies 1" 

@exercies_1.route("/about-me")
def about_me():
    return render_template("about_me.html")

@exercies_1.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  exercies_1.run(debug = True)
 

# render_template('index.html')