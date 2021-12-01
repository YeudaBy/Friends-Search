from flask import Flask, request, jsonify, render_template, Response
from pony.orm import db_session
from queries import search as find, Parse

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():

    error = {}
    response = {}

    query = request.args.get("query") or request.args.get("q")
    episode = request.args.get("episode") or request.args.get("e")
    season = request.args.get("season") or request.args.get("s")
    limit = request.args.get("limit") or request.args.get("l")
    lang = request.args.get("lang") or request.args.get("language")

    if not query:
        error = {"error": "a `query` is required."}

    if lang and len(lang) != 2:
        error = {"error": "`language` must be two characters, e.g. `EN`."}

    if episode and not episode.isdigit():
        error = {"error": "`episode` index must be a digit."}

    if season and not season.isdigit():
        error = {"error": "`season` index must be a digit."}

    if limit and not limit.isdigit():
        error = {"error": "`limit` must be a digit."}

    if error:
        return jsonify(error), 400

    with db_session:
        results = [Parse(i).__dict__ for i in find(
            query=query,
            season=season,
            episode=episode,
            limit=limit,
            lang=lang
        )]
        response["count"] = len(results)
        response["results"] = results

        # if response["count"] == 0:
        #     return Response(status=404)

        return jsonify(response), 200


app.run()
