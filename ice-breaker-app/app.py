from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    result, picture_url = ice_break_with(name)
    return jsonify({"summary_and_facts": result.to_dict(), "picture_url": picture_url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
