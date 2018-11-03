import random,x request
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    movie_list = ["Batman", "Finding Nemo", "Big Hero 6", "Finding Dory", "Star Trek: The Wrath Of Khan"]
    chosen_word = random.choice(movie_list)
    chosen_word2 = random.choice(movie_list)
    return """
	<html>
		<center>
			<h1>Movie of the Day</h1>
			<h2>{0}</h2>
			<h1> Movie Of The Day</h1>
			<h2>{1}</h2>
			<form id = "add-movie" action="/create"method="POST"
				<label for="add-movie">Add movie:</label>
				<br />
				<input id="add-movie" type="text"">
				<br />
				<input id="submit" type="submit" name = "submit">
			<br />
			<br />
				<label for ="crossout-movie">I want to cross out:</label>
				<br>
				<select id="crossout-movie" size="5">
					<option value="batman">Batman</option>
					<option value="finding-nemo">Finding Nemo</option>
					<option value="big-hero-6">Big Hero 6</option>
					<option value="finding-dory">Finding Dory</option>
					<option value="khaan">Star Trek: Wrath Of Khan</option>
				</select>
				<br />
				<input id="submit2" type="submit">
			</form>
		</center>
	</html>	
    """.format(chosen_word,chosen_word2)

def fetch_info():
	


app.run()
