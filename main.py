from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
  <html>
    <head>
      <style>
        form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}

        textarea {{
            margin: 10px -;
            width: 540px;
            height: 120px
        }}

      </style>
    </head>
    <body>
      <form action="/encrypt" method='POST'>
        <label><strong>Rotate by: </strong>
        <input type="text" name="rot" value="0"></input></label>
        <br>
        <br>
        <textarea name="text">{0}</textarea>
        <br>
        <br>
        <button type="submit" name="Submit query">Submit query</button>
      </form>
    </body>
  </html>
"""


@app.route("/encrypt", methods=['POST'])
def encrypt():
  rotation = request.form['rot']
  rotation = int(rotation)
  msg = request.form['text']
  encrypted = rotate_string(msg, rotation)
  return form.format(encrypted)

@app.route("/")
def index():
    return form.format("")

app.run()

