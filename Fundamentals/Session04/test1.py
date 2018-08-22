# users_list =  [
#     {
#     "name" : "Nguyen Anh Quan",
#     "age" : 16
#     },
#     {
#     "name" : "Huynh Tuan Anh",
#     "age" : 23
#     }
# ]
# print(users_list)
# print(type(users_list))

user = {
	"quan" : {
			"name" : "Nguyen Anh Quan",
            "age" : 16
    },
"tuananh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 23
    }
}
# print(user)

def check_profile(username):
    if username in user:
        print(user[username]["name"], user[username]["age"])
    else:
        print("User not found")
    # do_not_have_user = True
    # while do_not_have_user:
# for key in user.keys():
    # if key == a:
    #     do_not_have_user = False
    #     break               
    # else:
    #     print("User not found")
    #     break
        
# check_profile("tuananh")
check_profile("ha")