from flask import Flask, request
from caesar import rotate_string

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
        <label><strong>Rotate by: </strong>
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

@app.route("/", methods=['POST'])
def encrypt():
  rotation = request.rot
  sentence = request.text
  response = rotate_string(rotation, sentence)
  return '<h1>' + response + '</h1>'

app.run()

