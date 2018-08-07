from flask import *
pilot_app = Flask(__name__)
import mlab
from models.nguoi_cho_thue import nguoi_cho_thue
from customers.customers import customers
from datetime import datetime


mlab.connect()

# class nguoi_cho_thue(Document):
#     ten = StringField()
#     nam_sinh = IntField()
#     gtinh = IntField()
#     chieu_cao = IntField()
#     so_dt = StringField()
#     dia_chi = StringField()
#     tinh_trang = BooleanField()

# nguoi_cho_thue_moi = nguoi_cho_thue(
#     ten = "Nguyễn Văn Cường",
#     nam_sinh = 1996,
#     gtinh = 1,
#     chieu_cao = 166,
#     so_dt = "01764731804543",
#     dia_chi = "Đông Anh - Hà Nội",
#     tinh_trang = False
#     )   

# nguoi_cho_thue_moi = nguoi_cho_thue(
#     ten = "Nguyễn Văn Cường",
#     nam_sinh = 1996,
#     gtinh = 1,
#     chieu_cao = 166,
#     so_dt = "01764731804543",
#     dia_chi = "Đông Anh - Hà Nội",
#     tinh_trang = False
#     )   

# nguoi_cho_thue_moi.save()

@pilot_app.route('/')
def index():
    return render_template('index.html')

@pilot_app.route("/customers")
def customer():
    all_customers = customers.objects()
    return render_template("customers.html", all_customers = all_customers)

@pilot_app.route("/delete/<model_id>")
def delete(model_id):
    have_model = nguoi_cho_thue.objects.with_id(model_id)
    if have_model is not None: 
        have_model.delete()
        return redirect(url_for("admin"))
    else:
        return ("Not found.")
    
@pilot_app.route("/new_model", methods = ["GET", "POST"])
def new_model():
    if request.method == "GET":
        return render_template("new_model.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone_numb = form["phone_numb"]
        option = form["gender"]
        add_model = nguoi_cho_thue(
            name = name,
            yob = yob,
            phone_numb = phone_numb"
        )
        add_model.save()
        return redirect(url_for("admin"))

@pilot_app.route("/search/<gtinh>")
def search(gtinh):
    tat_ca_nguoi_cho_thue = nguoi_cho_thue.objects(gtinh = gtinh, nam_sinh__lte = 2018, dia_chi__contains = "Hà Nội")
    return render_template("search.html", tat_ca_nguoi_cho_thue = tat_ca_nguoi_cho_thue)

@pilot_app.route("/find")
def first_10_male_customers():
    all_customers = customers.objects(gender = 1, contacted = 0)[:10]
    return render_template("first_10_male_customers.html", all_customers = all_customers)

@pilot_app.route("/admin")
def admin():
    all_models = nguoi_cho_thue.objects()
    return render_template("admin.html", all_models = all_models)

if __name__ == '__main__':
  pilot_app.run(debug=True)



 