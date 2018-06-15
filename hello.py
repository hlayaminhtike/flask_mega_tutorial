from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/indes")
def index():
    return "This is index"
if __name__ == "__main__":
    app.run(debug=True)
