import mlab
from classes.classes import *
from datetime import datetime
from flask import *
pilot_app = Flask(__name__)

mlab.connect()
pilot_app.secret_key = "123"

#Home page
@pilot_app.route("/")
def index():
    return render_template("index.html")

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
        admin = Users.objects(log_in__exact = log_in, 
        password__exact = password, is_admin = True)
        if len(admin) != 0:
            admin_id = admin[0].id
            session["admin_logged_in"] = True
            session["admin_logged_in_id"] = str(admin_id)
            all_models = Models.objects()
            return render_template("admin.html", all_models = all_models)  
        elif len(admin) == 0: 
            return ("Sai tài khoản.")

#Admin page
@pilot_app.route("/admin")
def admin():
    if "admin_logged_in" in session:
        all_models = Models.objects()
        return render_template("admin.html", all_models = all_models)
    else:   
        return redirect(url_for("admin_log_in"))
#Orders page
@pilot_app.route("/orders-page")
def show_all_orders():
    if "admin_logged_in" in session:
        all_orders = Orders.objects(is_accecpted = False)
        return render_template("orders-page.html", all_orders = all_orders)
    else:   
        return redirect(url_for("admin_log_in"))

#Accpect order
@pilot_app.route("/accept_orders/<order_id>/<model_id>/<user_id>")
def accept_orders(order_id, model_id, user_id):
    if "admin_logged_in" in session:
        order = Orders.objects.with_id(order_id)
        if len(order) != 0:
            model = Models.objects.with_id(model_id)
            if len(model) != 0:
                model.update(set__status = 0)
                order.update(set__is_accecpted = True)
                return ("Đã phê duyệt.")    
            elif len(model) == 0:
                return ("Người mẫu hiện không còn trên hệ thống.")
        elif len(order) == 0:
            return redirect(url_for("show_all_orders"))


# Admin log out
@pilot_app.route("/admin-log-out")
def admin_log_out():
    del session["admin_logged_in"]
    return redirect(url_for("index"))

#Show all models
@pilot_app.route("/show-all-models")
def show_all_models():
    if "user_logged_in" in session:
        all_models = Models.objects()
        return render_template("models.html", all_models = all_models)
    else:
        return redirect(url_for("user_log_in"))

#Show all customers
@pilot_app.route("/show-all-customers")
def show_all_customers():
    if "admin_logged_in" in session:
        all_customers = Customers.objects()
        return render_template("customers.html", 
        all_customers = all_customers)
    else:
        return redirect(url_for("admin_log_in"))

#Delete model
@pilot_app.route("/delete/<model_id>", methods = ["GET", "POST"])
def delete(model_id):
    model = Models.objects.with_id(model_id)
    if "admin_logged_in" in session:
        if len(model) != 0: 
            model.delete()
            return redirect(url_for("admin"))
        elif len(model) == 0:
            return ("Not found.")
    else:
        return redirect(url_for("admin_log_in"))

#Update model information
@pilot_app.route("/update-model/<model_id>", methods = ["GET","POST"])
def update_model(model_id):
    model = Models.objects.with_id(model_id)
    if request.method == "GET":
        if "admin_logged_in" in session:
            if len(model) != 0:
                return render_template("update-model.html", model = model)
            elif len(model) == 0: 
                return redirect(url_for("admin_log_in"))
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
        model = Models.objects(name = name, yob = yob, 
        gender = gender_to_add, height = height, phone_numb = phone_numb, 
        avatar = avatar, description = description, 
        measurements = measurements, status = status_to_add)
        if len(model) != 0:
            return render_template("results.html", model = model)
        elif len(model) == 0:
            return ("Không có kết quả.")
            
#Add new model
@pilot_app.route("/new-model", methods = ["GET", "POST"])
def add_new_model():
    if request.method == "GET":
        if "admin_logged_in" in session:
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
            log_in = sign_in,
            password = password,
        )
        new_user.save()
        return redirect(url_for("user_log_in"))

#User log in
@pilot_app.route("/user-log-in", methods = ["GET", "POST"])
def user_log_in():
    if request.method == "GET":  
        if "user_logged_in" in session:
            return redirect(url_for("show_all_models"))
        else:
            return render_template("user-log-in.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        password = form["password"]
        user = Users.objects(log_in__exact = name, 
        password__exact = password, is_admin = False)
        if len(user) != 0:
            user_id = user[0].id
            session["user_logged_in"] = True
            session["user_logged_in_id"] = str(user_id)
            return redirect(url_for("show_all_models"))
        elif len(user) == 0:
            return ("Sai tài khoản.")

#Models detail
@pilot_app.route("/detail/<model_id>")
def detail(model_id):
    if "user_logged_in" in session:
        model = Models.objects.with_id(model_id)
        return render_template("detail.html", model = model)
    else:
        return redirect(url_for("user_log_in"))

#Search models information
# @pilot_app.route("/search", methods = ["GET", "POST"])
# def search_model():
#     if method.request == "GET":
#         if "user_logged_in" in session:
#             return render_template("search_model.html")
#         else:
#             return redirect(url_for("user_log_in"))
#     elif method.request == "POST":
#         form = request.form
#         name = form["name"]
#         yob = form["yob"]
#         gender_value = form["gender"]
#         if gender_value == "Nam":
#             gender_to_find = 1
#         elif gender_value == "Nữ":
#             gender_to_find = 0 
#         height = form["height"]
#         phone_numb = form["phone_numb"]
#         address = form["address"]
#         description = form["description"]
#         measurements = form["measurements"]
#         model = Models.objects(name = name, yob = yob, gender = gender_to_find, 
#         height = height, phone_numb = phone_numb, address, description = description, measurements = measurements)
#         return render_template("search_show.html", model = model)

# User log out
@pilot_app.route("/user-log-out")
def user_log_out():
    del session["user_logged_in"]
    return redirect(url_for("index"))
         
#User orders service
@pilot_app.route("/order-service/<model_id>/<user_id>")
def order_service(model_id, user_id):
    if "user_logged_in" in session:
        order = Orders.objects(model_id = model_id, user_id = user_id)
        if len(order) == 0:
            new_order = Orders(
                model_id = model_id,
                user_id = user_id,
                order_time = datetime.now()
            )
            new_order.save()
            return ("Đã gửi yêu cầu.")
        elif len(order) != 0:
            return ("Bạn đã gửi yêu cầu. Xin chờ xác nhận.")

if __name__ == '__main__':
  pilot_app.run(debug=True)



 