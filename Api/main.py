from flask import Flask, request, jsonify, render_template
from pony.orm import db_session
from queris import search as find, Parse

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    error = {}
    res = {}
    query = request.args.get("query") or request.args.get("q")
    episode = request.args.get("episode") or request.args.get("e")
    season = request.args.get("season") or request.args.get("s")

    if not query:
        error = {"error": "a query is required."}

    if (episode and not season) or (season and not episode):
        error = {"error": "When one is used, both are required: Episode and Season."}

    if error:
        return jsonify(error)

    with db_session:
        results = [Parse(i).__dict__ for i in find(query, season, episode)]
        res["count"] = len(results)
        if len(results) > 30:
            res["note"] = "Too many results. Returns only the first 30 results. Prefer a search by chapter and season."
            if not request.args.get("limit"):
                results = results[:30]
        res["results"] = results
        return jsonify(res)


app.run()
