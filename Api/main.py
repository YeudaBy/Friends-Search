from flask import Flask, request, jsonify, redirect
from flask_cors import CORS, cross_origin
from pony.flask import Pony

from Api.admin import verify_sentence, report_sentence, review_content
from Api.utils import AppConfig
from DB.querys import (all_languages, is_language_exist, sentence_random, parse, sentence_by_id, search_sentence,
                       like_sentence)

# -------- Flask initialization ----------
app = Flask(__name__)
Pony(app)

# --------- CORS configuration ----------
cors = CORS(app)

# ----- App configuration -------
app.config.from_object(AppConfig)


# ------ Statistics --------
@app.before_request
def _x():
    print(request)


# -------- Admin methods ----------
app.add_url_rule(rule="/sentence/<int:_id>/verify", view_func=verify_sentence, methods=["POST"])
app.add_url_rule(rule="/sentence/<int:_id>/report", view_func=report_sentence, methods=["POST"])
app.add_url_rule(rule="/sentence/<int:_id>/review", view_func=review_content, methods=["POST"])


# ------ Docs --------
@cross_origin()
@app.route("/docs")
def home():
    """ home page """
    return redirect("https://friends-search.readthedocs.io/")


# -------- GET methods ----------
@cross_origin()
@app.route("/language")
def languages():
    """ return dict of all languages supported """
    return {"ok": True, "results": all_languages()}, 200


@cross_origin()
@app.route("/language/<language>")
def get_language(language):
    """ return if language exists """
    response = is_language_exist(language)
    if response:
        return {"ok": True, "results": response}, 200
    return {"ok": True, "error": "language not found or noe supported yet"}, 404


@cross_origin()
@app.route("/sentence/random/")
def random_sentence():
    """ return list of random sentences
     optional args: language [default=ag]
     """
    random_results = sentence_random(language=request.args.get("language"))
    response = [parse(sentence) for sentence in random_results]
    return {"ok": True, "results": response}, 200


@cross_origin()
@app.route("/sentence/<int:_id>")
def get_by_id(_id):
    """ get the sentence by specific id """
    data = parse(sentence_by_id(_id))
    return ({"ok": True, "results": data}, 200) if data else (
        {"ok": False, "error": "sentence not found"}, 404)


@cross_origin()
@app.route("/sentence/search")
def search():
    """ search sentence
    required args: query
    optionals args: limit [default=50], language [default=ag]
    """
    error = {}
    response = {}

    query = request.args.get("query") or request.args.get("q")
    limit = request.args.get("limit") or request.args.get("l") or 50  # set 50 for limit as default
    lang = request.args.get("language") or request.args.get("lang") or "ag"  # set language default to All languages

    # costume error
    if query == "make_error":
        return jsonify({"error": "costume error"})  # demo error for debugging

    if not query:
        error = {"error": "a `query` is required"}  # when `query` does not provided

    if lang and len(lang) != 2:
        error = {"error": "`language` must be two characters"}  # wrong language format

    if limit and isinstance(limit, str) and not limit.isdigit():
        error = {"error": "`limit` must be a digit"}  # `limit` parameter does not number

    if error:
        return {"ok": False, "error": error}, 400

    results = [parse(result) for result in search_sentence(
        query=query,
        limit=int(limit),
        lang=lang
    )]
    response["ok"] = True
    response["count"] = len(results)
    response["results"] = results

    return jsonify(response), 200


# ------ POST methods -------


@cross_origin()
@app.route("/sentence/<int:_id>/like", methods=['POST'])
def _like_sentence(_id):
    """ react like to a sentence """
    if like_sentence(_id):
        return {"ok": True}, 200
    return {"ok": False}, 400


if __name__ == '__main__':
    app.run()
