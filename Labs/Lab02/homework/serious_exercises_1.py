# quan = ["Quan", 22, "Chua", "Ha Noi", 2, 3, ["PES", "Ping pong"]]
#dictionary
# key: value
# person = {
#     "name": "Quan",
#     "age": 22,
#     "ex": 2,
#     "favs": ["PES", "Ping pong"]
# }
# key = "school"
# if key in person:
#     print(person[key])
# else: 
#     print("Not found.")

# print(person[key])
# print(person)
# person["school"] = "Nguyen Gia Thieu"
# print(person)

# for key in person.keys():
#     print(key, end = "\t")

# for key, vars in person.items():
#     print(key, vars)

# for value in person.values():
#     print(value)
    
# person["name"] = "Quan kull"
# print(person)

# del person["ex"]
# print(person)

# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# a = input("fruit: ")
# for key, value in prices.items():
#     have_fruit = False
#     if a == key:
#         have_fruit = True
#     if have_fruit:
#         print(a)
#         print("prices: ", prices[a])

# a_list = [1, 2, 3, 4, 5]
# for index, value in enumerate(a_list):
#     print(index, value)

# boxes = [
#     {"x": 1, "y": 1},
#     {"x": 2, "y": 2},
#     {"x": 3, "y": 3},
# ]

# print(boxes[1])
# print(type(boxes[1]))

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
connection = urlopen(url)
data = connection.read()
html_content = data.decode("utf-8")
parserd_to_html = BeautifulSoup(html_content, "html.parser")
section_content = parserd_to_html.find_all("div", "section-content")
# print(section_content)
ROI = section_content[1]
# print(ROI)
# myfile = open("top_songs.html", "wb")
# myfile.write(data)
# myfile.close()
# print(type(ROI))
ul_tag = ROI.find("ul")
# print(ul_tag.prettify())
li_list = ul_tag.find_all("li")
# print(li_list)
list_top_songs_and_artists = []
for li in li_list:
    download_songs = YoutubeDL()
    songs_name_and_artists = {}
    # numerical_order = li.find("strong")
    songs_name = li.find("h3")
    artists = li.find("h4")
    # order = numerical_order.string
    content_songs_name = songs_name.string
    content_artists = artists.string
    # songs_name_and_artists["Numerical order"] = order
    songs_name_and_artists["default_search"] = "ytsearch"
    songs_name_and_artists["max_downloads"] = 1
    songs_name_and_artists["names"] = content_songs_name
    songs_name_and_artists["artists"] = content_artists
    download_songs = YoutubeDL(songs_name_and_artists)
    print(songs_name_and_artists)
    download_songs.download(["haha"])
    # list_top_songs_and_artists.append(songs_name_and_artists)
# pyexcel.save_as(records = list_top_songs_and_artists, dest_file_name = "top_songs.xlsx")


# for songs_and_artists in list_top_songs_and_artists:
    # order = 0
    # download_options = {}
    # download_options = songs_and_artists

    

