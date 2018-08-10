from flask import *
pilot_app = Flask(__name__)
import mlab
from models.models import Models
from customers.customers import Customers
from users.users import Users
from admins.admins import Admins
from orders.orders import Orders
from datetime import datetime

mlab.connect()
pilot_app.secret_key = "123"

#Home page
@pilot_app.route("/")
def index():
    return render_template("index.html")

#User sign in
@pilot_app.route("/user-sign-in", methods = ["GET", "POST"])
def user_sign_in():
    if request.method == "GET":
        return render_template("user-sign-in.html")
    elif request.method == "POST":
        form = request.form
        full_name = form["full-name"]
        email = form["email"]
        sign_in = form["sign-in"]
        password = form["password"]
        new_user = Users(
            full_name = full_name,
            email = email,
            sign_in = sign_in,
            password = password
        )
        new_user.save()
        return redirect(url_for("user_log_in"))

#User log in
@pilot_app.route("/user-log-in", methods = ["GET", "POST"])
def user_log_in():
    if request.method == "GET":
        # all_users = Users.objects()
        # for user in all_users:
            # if user.id in session:  
        if "user_logged_in" in session:
            return redirect(url_for("show_models"))
        else:
            return render_template("user-log-in.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        password = form["password"]
        have_user = Users.objects(sign_in__exact = name, 
        password__exact = password)
        if have_user is not None:
            user_id = have_user[0].id
            session["user_logged_in"] = str(user_id)
            return redirect(url_for("show_models"))
        else:
            return ("Sai tài khoản.")

#Show all customers
@pilot_app.route("/customers")
def customer():
    all_customers = Customers.objects()
    return render_template("customers.html", all_customers = all_customers)

#Models detail
@pilot_app.route("/detail/<model_id>")
def detail(model_id):
    if "user_logged_in" in session:
    # for user in all_users:
        # if str(user.id) in session:
        model = Models.objects.with_id(model_id)
        return render_template("detail.html", model = model)
    else:
        return redirect(url_for("user_log_in"))

#Update model information
@pilot_app.route("/update-model/<model_id>", methods = ["GET","POST"])
def update_model(model_id):
    model = Models.objects.with_id(model_id)
    if request.method == "GET":
        return render_template("update-model.html", model = model)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        gender_value = form["gender"]
        if gender_value == "Nam":
            gender_to_add = 1
        elif gender_value == "Nữ":
            gender_to_add = 0 
        height = form["height"]
        phone_numb = form["phone_numb"]
        address = form["address"]
        avatar = form["avatar"]
        description = form["description"]
        measurements = form["measurements"]
        status_value = form["status"]
        if status_value == "Rảnh":
            status_to_add = 0
        elif status_value == "Bận":
            status_to_add = 1
        model.update(set__name = name, set__yob = yob, 
        set__gender = gender_to_add, set__height = height, set__phone_numb = phone_numb, 
        set__avatar = avatar, set__description = description, 
        set__measurements = measurements, set__status = status_to_add)
        model.reload()
        return redirect(url_for("admin"))

#Delete model
@pilot_app.route("/delete/<model_id>")
def delete(model_id):
    have_model = Models.objects.with_id(model_id)
    if have_model is not None: 
        have_model.delete()
        return redirect(url_for("admin"))
    else:
        return ("Not found.")

#Add new model
@pilot_app.route("/new-model", methods = ["GET", "POST"])
def new_model():
    if request.method == "GET":
        return render_template("new-model.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone_numb = form["phone_numb"]
        gender_value = form["gender"]
        if gender_value == "1":
            gender_to_add = 1
        elif gender_value == "0":
            gender_to_add = 0
        add_model = Models(
            name = name,
            yob = yob,
            gender = gender_to_add,
            phone_numb = phone_numb,
        )
        add_model.save()
        return redirect(url_for("admin"))

#Search models information
@pilot_app.route("/search/<gender>")
def search(gender):
    all_models = Models.objects(gender = gender, yob__lte = 2018)
    return render_template("search.html", all_models = all_models)

#Show all models
@pilot_app.route("/search")
def show_models():
    all_models = Models.objects()
    return render_template("models.html", all_models = all_models)

#Find first 10 male customers not yet contacted
@pilot_app.route("/find")
def first_10_male_customers():
    all_customers = Customers.objects(gender = 1, contacted = 0)[:10]
    return render_template("first-10-male-customers.html", 
    all_customers = all_customers)

#Admin page
@pilot_app.route("/admin", methods = ["GET", "POST"])
def admin():
    if request.method == "GET":
        if "admin_logged_in" in session:
    # all_admins = Admins.objects()
    # for admin in all_admins:
        # if str(admin.id) in session:
            all_models = Models.objects()
            return render_template("admin.html", all_models = all_models)
        else:   
            return redirect(url_for("admin_log_in"))

# User log out
@pilot_app.route("/user-log-out")
def user_log_out():
    # have_user = Users.objects.with_id(admin_id)
    # for user in have_user:
        # if str(user.id) in session:
            # del session[str(user.id)]
    del session["user_logged_in"]
    return redirect(url_for("index"))
         
# Admin log out
@pilot_app.route("/admin-log-out")
def admin_log_out():
    del session["admin_logged_in"]
    return redirect(url_for("index"))

#Admin log in
@pilot_app.route("/admin-log-in", methods = ["GET", "POST"])
def admin_log_in():
    if request.method == "GET":
        if "admin_logged_in" in session:
            all_models = Models.objects()
            return render_template("admin.html", all_models = all_models)  
        else:
            return render_template("admin-log-in.html")
    elif request.method == "POST":
        form = request.form
        log_in = form["name"]
        password = form["password"]
        have_admin = Admins.objects(log_in__exact = log_in, 
        password__exact = password)
        if have_admin is not None:
            admin_id = have_admin[0].id
            session["admin_logged_in"] = str(admin_id)
            all_models = Models.objects()
            return render_template("admin.html", all_models = all_models)  
        else: 
            return ("Sai tài khoản.")

#Order service
@pilot_app.route("/oder-service/<model_id>/<user_id>")
def order_service(model_id, user_id):
    new_order = Orders(
        model_id = model_id,
        user_id = user_id,
        order_time = datetime.now()
    )
    new_order.save()
    return redirect("Đã gửi yêu cầu.")

if __name__ == '__main__':
  pilot_app.run(debug=True)



 