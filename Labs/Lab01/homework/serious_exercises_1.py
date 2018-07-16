from gmail import GMail, Message
from random import choice

gmail = GMail("fakeacc.n2h@gmail.com", "tongpu123")
html_content = """
<p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập -&nbsp; Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">ĐƠN XIN NGHỈ HỌC</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">K&iacute;nh gửi: Giảng vi&ecirc;n lớp Code for everyone 19 - C4E 19 - Huỳnh Tuấn Anh</p>
<p style="text-align: left;">Em l&agrave;: Nguyễn Hải Phong</p>
<p style="text-align: left;">H&ocirc;m nay em viết&nbsp;đơn n&agrave;y xin&nbsp;được xin nghỉ học buổi thứ 3 \
ng&agrave;y 17/07/2018 v&igrave; l&yacute; do&nbsp;{{sickness}}.</p>
<p style="text-align: left;">Em xin hứa l&agrave;m b&agrave;i&nbsp;đầy&nbsp;đủ.</p>
<p style="text-align: left;">Em xin cảm&nbsp;ơn.</p>
<p style="text-align: right;">&nbsp;</p>
"""
list_reasons = ["em thích", "nhà em có việc", "chị em sinh em bé"]
html_reason = html_content.replace("{{sickness}}", choice(list_reasons))
msg = Message("Test Message", to = "fakeacc.n2h@gmail.com", html = html_reason)

from datetime import datetime, time
if datetime.now().hour == 13 and datetime.now().minute == 52:
    gmail.send(msg)
