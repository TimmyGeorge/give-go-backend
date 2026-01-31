from flask import Flask, redirect, render_template, request

app=Flask(__name__, static_url_path='/static')


@app.route('/player/signin')
def player_signin():
    return render_template("player/signin.html")

@app.route('/player/signup', methods=['GET'])
def player_signup_get():
    return render_template("player/signup.html")

@app.route('/player/signup', methods=['POST'])
def player_signup_post():
    return redirect('/player/signin')


@app.route('/poster/signin')
def poster_signin():
    return render_template("poster/signin.html")

@app.route('/poster/signup')
def poster_signup():
    email: str = request.form["email"]
    username: str = request.form["username"]
    password1: str = request.form["password1"]
    password2: str = request.form["password2"]

    if password1 != password2:
        return render_template("poster/signup.html", error="Passwords do not match")

    return render_template("poster/signup.html")


"""
POST /player/signup
- PARAMETERS
	- email : string
	- username: string
	- password1: string
	- password2: string
- RESPONSE
	- if the passwords do not match
		- redirect to the same page with an error message
	- if there is a player with this email and username (in database)
		- redirect to the same page with an error message
	- else
		- redirect the player to the /player/signin page 
			with a success message of successfully signing up

"""

@app.route('/')
def root():
    return render_template("root.html")


app.run('0.0.0.0',81) #Runs the development server.
