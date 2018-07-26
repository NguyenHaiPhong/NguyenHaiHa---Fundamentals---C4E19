from flask import Flask, render_template
serious_excercises_2 = Flask(__name__)


@serious_excercises_2.route("/")
def index():
    return ("Serious Exercies 2")

@serious_excercises_2.route("/user/<username>")
def user_name(username):
    user = {
        "quan" : {
                "name" : "Nguyen Anh Quan",
                "age" : 16
        },
    "tuananh" : {
                "name" : "Huynh Tuan Anh",
                "age" : 23
        },
        "ha": {
                "name": "Nguyen Hai Ha",
                "age": 22
        }
    }
    # if username in user:
    #     return (user[username]["name"], user[username]["age"])
        
    # else:
    #     return ("User not found")
    return render_template("profile.html", user = user, username = username)

if __name__ == '__main__':
    serious_excercises_2.run(debug=True)
 