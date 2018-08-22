from flask import *
import mlab
from models.video import Video
from youtube_dl import YoutubeDL

app = Flask(__name__)
app.secret_key = "123"

mlab.connect()

@app.route("/admin", methods = ["GET", "POST"])
def admin():
    if "logged_in" in session:
        if session["logged_in"]:
            if request.method == "GET":
                all_videos = Video.objects()
                return render_template("admin.html", all_videos = all_videos)
            elif request.method == "POST":
                form = request.form
                link = form["link"]
                ydl = YoutubeDL()
                data = ydl.extract_info(link, download=False)
                title = data["title"]
                thumbnail = data["thumbnail"]
                views = data["view_count"]
                youtube_id = data["id"]
                new_vid = Video(
                    title = title,
                    link = link,
                    views = views,
                    thumbnail = thumbnail,
                    youtube_id = youtube_id
                )
                new_vid.save()
                return redirect(url_for("admin"))
    else:
        return ("Access dinied.")

@app.route("/log-out")
def log_out():
    del session["logged_in"]
    return redirect(url_for("index"))

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        user_name = form["user_name"]
        password = form["password"]
        if user_name == "admin" and password == "admin":
            session["logged_in"] = True
            return redirect(url_for("admin"))
        else:
            return ("Sai đăng nhập.")

@app.route("/detail/<youtube_id>")
def detail(youtube_id):
    return render_template("detail.html", youtube_id = youtube_id)

@app.route("/")
def index():
    all_videos = Video.objects()
    return render_template("index.html", all_videos = all_videos)

if __name__ == '__main__':
  app.run(debug=True)
 