# 1. Download webpage

from urllib.request import urlopen
from bs4 import BeautifulSoup
# html = urlopen("http://s.cafef.vn/bao-cao-\
# tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn").read().decode('utf-8')
# print(html)
# 1.1. Open a connection
url = "http://dantri.com.vn"
connection = urlopen(url)
# 1.2. Read data

data = connection.read()
# 1.3. Decode

html_content = data.decode("utf-8")
# print(html_content)

# import urllib.request
# link = "http://dantri.com.vn/su-kien.htm"
# destination_filename = "dantri.html"
# urllib.request.urlretrieve(link, destination_filename)

# myfile = open("dantri.html", "wb")
# myfile.write(data)
# myfile.close()

# 2. Extract ROI (Region of interest)

soup = BeautifulSoup(html_content, "html.parser")
ul_tag = soup.find("ul", "ul1 ulnew") 
print(type(ul_tag))
# print(type(ul_tag))
print(ul_tag.prettify())

# 3. Extract information
li_list = ul_tag.find_all("li")
print(type(li_list))
print(li_list)
list_title_and_content_of_dan_tri = []
for li in li_list:
    # h4 = li.find("h4")
    # a = h4.find("a")
    a = li.h4.a
# print(a.prettify())
    dict_in_list = {}
    content = a.string
    href = url + a["href"]
    dict_in_list.update({"Content": content})
    dict_in_list.update({"Link": href})
    list_title_and_content_of_dan_tri.append(dict_in_list)
# print(li.prettify())
# 4. Save data to excel 
# import pyexcel
# a_list_of_dictionaries = [
#         {
#         "Name": 'Adam',
#         "Age": 28
#         },
#         {
#          "Name": 'Beatrice',
#          "Age": 29
#         },
#         {
#          "Name": 'Ceri',
#          "Age": 30
#         },
#         {
#          "Name": 'Dean',
#          "Age": 26
#         }
# ]
# pyexcel.save_as(records = list_title_and_content_of_dan_tri, dest_file_name = "demo1.xlsx")