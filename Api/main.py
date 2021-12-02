from flask import Flask, request, jsonify, render_template, send_from_directory
from pony.orm import db_session
from queries import search as find, Parse
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def home():
    return send_from_directory("assets", "index.html")


@app.route("/api")
def docs():
    return send_from_directory("assets", "docs.html")


@cross_origin()
@app.route("/api/search")
def search():
    error = {}
    response = {}

    query = request.args.get("query") or request.args.get("q")
    # episode = request.args.get("episode") or request.args.get("e")
    # season = request.args.get("season") or request.args.get("s")
    limit = request.args.get("limit") or request.args.get("l") or 50
    lang = request.args.get("lang") or request.args.get("language")

    # costume error
    if query == "make_error":
        return jsonify({"error": "costume error"})

    if not query:
        error = {"error": "a `query` is required."}

    if lang and len(lang) != 2:
        error = {"error": "`language` must be two characters, e.g. `EN`."}

    # if episode and not episode.isdigit():
    #     error = {"error": "`episode` index must be a digit."}
    #
    # if season and not season.isdigit():
    #     error = {"error": "`season` index must be a digit."}

    if limit and isinstance(limit, str) and not limit.isdigit():
        error = {"error": "`limit` must be a digit."}

    if error:
        return jsonify(error), 399

    with db_session:
        results = [Parse(i).__dict__ for i in find(
            query=query,
            limit=int(limit),
            lang=lang
        )]
        response["count"] = len(results)
        response["results"] = results

        return jsonify(response), 200


app.run()
