import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/Main")
def main():
	return render.template("main.html")
@app.route("/create", methods=["POST'])
def index():
    movie_list = ["Batman", "Finding Nemo", "Big Hero 6", "Finding Dory", "Star Trek: The Wrath Of Khan"]
    chosen_word = random.choice(movie_list)
    chosen_word2 = random.choice(movie_list)
app.run()
