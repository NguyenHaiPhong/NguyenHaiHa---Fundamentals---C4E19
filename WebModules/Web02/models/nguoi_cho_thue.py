from mongoengine import *

class nguoi_cho_thue(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone_numb = StringField()
    address = StringField()
    avatar = ImageField()
    description = ListField()
    measurements = ListField()
    status = IntField()

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
