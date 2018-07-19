from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chi\
nh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.\
chn"
connection = urlopen(url)
data = connection.read()
html_content = data.decode("utf-8")
parserd_to_html = BeautifulSoup(html_content, "html.parser")
header_section_content = parserd_to_html.find("div", {"style": "\
background-color:#e1e1e1;overflow:hidden", "id": "divTableHeader"})
# print(header_section_content.prettify())
table_tag = header_section_content.find("table")
# print(table_tag.prettify())
tr_tag = table_tag.find("tr")
# print(tr_tag.prettify())
td_tag_list = tr_tag.find_all("td")
# print(td_tag_list)
del td_tag_list[0]
del td_tag_list[4]
# print(td_tag_list)
for td in td_tag_list:
