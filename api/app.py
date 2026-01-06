from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Auge Predict API — Experimental"

if __name__ == "__main__":
    app.run(debug=True)
