from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello TAA, Mo here, pass to me!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
