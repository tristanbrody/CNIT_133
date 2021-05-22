from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbar
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hw8.html")


@app.route("/gethint")
def get_hint():
    user_input = request.args.get("firstname", None)
    res = {"hint": [], "hint_available": False}
    if user_input is not None:
        res["hint"] = [name for name in NAMES if name.lower().startswith(user_input)]
    if len(res["hint"]) > 0:
        res["hint_available"] = True
    return jsonify(res)


NAMES = [
    "Anna",
    "Brittany",
    "Cinderella",
    "Diana",
    "Eva",
    "Fiona",
    "Gunda",
    "Hege",
    "Inga",
    "Johanna",
    "Kitty",
    "Linda",
    "Nina",
    "Ophelia",
    "Petunia",
    "Amanda",
    "Raquel",
    "Cindy",
    "Doris",
    "Eve",
    "Evita",
    "Sunniva",
    "Tove",
    "Unni",
    "Violet",
    "Liza",
    "Elizabeth",
    "Ellen",
    "Wenche",
    "Vicky",
]
