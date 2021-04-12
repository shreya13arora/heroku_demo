from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Heroku!"

@app.route("/someendpoints")
def firstendpoint():
    return "This is my first path on heorku"

if __name__ == "__main__":
    @app.run()