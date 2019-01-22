"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = [

    'leave me', 'omg ur ugly', 'I am unimpressed', 'what are thoooose',
    'noncoolio', 'dumb', 'meh', 'sad', 'poop' ]


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <a href="/hello">Hello</a></html>"""



@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="GET">
          What's your name? 
          <input type="text" name="person"><br><br>
          Select from the following:
          <br><br>
          <select name="compliment">
              <option value="awesome">Awesome</option>
              <option value="amazing">Amazing</option>
              <option value="fire">Fire</option>
          </select>
          <input type="submit" value="Submit">
          </form>
          <br><br>
          <br>
          <br>
          <br>
          What's your name? 
          <form action="/diss">
          <input type="text" name="person"><br><br>
           
            <input type="submit" value="Diss me">
            </form>
        
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss")
def diss_person():
    """ Disses the person."""

    player = request.args.get("person")

    diss = choice(DISSES)

    return"""
    <!doctype html>
    <html>
        <head>
            <title> A diss </title>
        </head>
        <body>
            Hi {}, you {}.
        </body>

    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
