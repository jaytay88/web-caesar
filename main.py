from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
  <html>
    <head>
      <style>
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }

        textarea {
            margin: 10px -;
            width: 540px;
            height: 120px
        }

      </style>
    </head>
    <body>
      <form method=['POST']>
        <label>Rotate by: 
        <input type="text" name="rot" value="0"></input></label>
        <br>
        <br>
        <textarea name-"text"></textarea>
        <br>
        <br>
        <button type="submit" name="Submit query">Submit query</button>
      </form>
    </body>
  </html>
"""

@app.route("/")
def index():
    return form

app.run()

