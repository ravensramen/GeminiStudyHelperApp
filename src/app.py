#testing different graphical libraries

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(debug=True)