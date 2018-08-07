from flask import *
river_app = Flask(__name__)
import mlab
from river import river

mlab.connect()

@river_app.route("/")
def all_rivers_in_africa_continent():
    all_rivers = river.objects(continent = "Africa")
    return render_template("ex-8.html", all_rivers = all_rivers)

@river_app.route("/ex-9")
def all_rivers_in_south_america_continent_length_lt_1000():
    all_rivers = river.objects(continent = "S. America", length__lt = 1000)
    return render_template("ex-9.html", all_rivers = all_rivers)

if __name__ == '__main__':
  river_app.run(debug=True)

