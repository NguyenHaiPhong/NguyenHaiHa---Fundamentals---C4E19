from mongoengine import *

class nguoi_cho_thue(Document):
    ten = StringField()
    nam_sinh = IntField()
    gtinh = IntField()
    chieu_cao = IntField()
    so_dt = StringField()
    dia_chi = StringField()
    tinh_trang = BooleanField()

nguoi_cho_thue_moi = nguoi_cho_thue(
    ten = "Nguyễn Văn Cường",
    nam_sinh = 1996,
    gtinh = 1,
    chieu_cao = 166,
    so_dt = "01764731804543",
    dia_chi = "Đông Anh - Hà Nội",
    tinh_trang = False
    )   

nguoi_cho_thue_moi = nguoi_cho_thue(
    ten = "Nguyễn Văn Cường",
    nam_sinh = 1996,
    gtinh = 1,
    chieu_cao = 166,
    so_dt = "01764731804543",
    dia_chi = "Đông Anh - Hà Nội",
    tinh_trang = False
    )   
