from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "It works!"

if __name__ == "__main__":
    print("Launching Flask server...")
    app.run(debug=True)
