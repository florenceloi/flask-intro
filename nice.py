from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    return """<!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        <p><a href="/hello">Go to hello </a></p>
      </body>
    </html>"""


@app.route('/hello')
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
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          Choose a Compliment:
            <select name="compliment-option">
              <option value="Awesome">Awesome</option>
              <option value="Great">Great</option>
              <option value="Wonderful">Wonderful</option>
              <option value="Fantastic">Fantastic</option>
            </select>
          <input type="submit">
          </form><br>
          <a href="/diss">Diss Instead</a>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment-option")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss():
    """Get user by name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Diss!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greeting-diss">
          <label>What's your name? <input type="text" name="person"></label><br>
          Choose a Diss:
            <select name="diss-option">
              <option value="Gross">Gross</option>
              <option value="Ugly">Ugly</option>
              <option value="Lame">Lame</option>
              <option value="Stinky">Stinky</option>
            </select>
          <input type="submit">
        </form>"""    


@app.route('/greeting-diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    diss = request.args.get("diss-option")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, diss)    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
