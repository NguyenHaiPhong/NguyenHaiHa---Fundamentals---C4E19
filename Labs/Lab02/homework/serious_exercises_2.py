from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel as pec

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connection = urlopen(url)
data = connection.read()
html_content = data.decode("utf-8")
parserd_to_html = BeautifulSoup(html_content, "html.parser")
header_content_section = parserd_to_html.find("div", {"style": "\
background-color:#e1e1e1;overflow:hidden", "id": "divTableHeader"})
# print(header_content_section.prettify())
table_header_tag = header_content_section.find("table")
# print(table_header_tag.prettify())
tr_header_tag = table_header_tag.find("tr")
# print(tr_header_tag.prettify())
td_header_tag_list = tr_header_tag.find_all("td")
# print(td_header_tag_list)
del td_header_tag_list[0]
del td_header_tag_list[4]
# print(td_header_tag_list)
# list_quarter = []
# for td in td_header_tag_list:
#     group_quarter = {}
#     quarter = td.string
#     group_quarter["Quarter"] = quarter
#     list_quarter.append(group_quarter)
# # print(list_quarter)
# pec.save_as(records = list_quarter, dest_file_name = "Ket qua hoat dong kinh doanh Cong ty co phan sua Viet Nam.xlsx")

# business_results = pec.get_sheet(file_name = "Ket qua hoat dong kinh doanh Cong ty co phan sua Viet Nam.xlsx")
body_content_section = parserd_to_html.find("div", {"style": "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;"})
# print(body_content_section.prettify())
table_body_tag = body_content_section.find("table", {"id": "tableContent", "cellpadding": "0", \
"cellspacing": "0", "width": "100%", "style": "border-top: solid 1px #e6e6e6;border-left:solid 1px #cccccc;border-bottom:solid 1px #cccccc"})
# print(table_body_tag.prettify())
# def adding_column_value(tr_tag_contain_title , td_tag_contain_value):
#     for 
tr_tag = table_body_tag.find("tr", {"class": "r_item ", "id": "01"})
# print(tr_tag.prettify())
td_tag_title = tr_tag.find("td", {"style": "width:32%;color:#014377;font-weight:bold;", "class": "b_r_c"})
title = td_tag_title.string
print(title)
print(type(title))
# print(td_tag_title.string)
list_td_tag_value = tr_tag.find_all("td", {"class": "b_r_c", "align": "right", \
 "style": "width:15%;padding:4px;color:#014377;font-weight:bold;"})
# print(list_td_tag_value)
title_1 = []
for td in list_td_tag_value:
    td_value = td.string   
    print(type(td_value))
    title_1.append(td_value)
# print(title_1)
# business_results.column += [title]
# business_results.column[title] = title_1
# business_results.save_as("Ket qua hoat dong kinh doanh Cong ty co phan sua Viet Nam_modify.xlsx")