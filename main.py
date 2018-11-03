import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/main")
def main():
	return render_template("main.html")
@app.route("/create", methods=["POST"])
def main_function():
    movie_list = ["batman", "finding nemo", "big hero 6", "finding dory", "star wars"]
    movie_day2 = request.form["movie_day"]
    movie_tommorow2 = request.form["movie_tommorow"]
	movie_choice = random.choice(movie_list)
	movie_day2 = movie_choice
	movie_tommorow2 = movie_choice
    return render_template("main.html", movie_day, movie_tommorow)
app.run()
