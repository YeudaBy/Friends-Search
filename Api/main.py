from flask import Flask, request, jsonify, render_template
from pony.orm import db_session
from flask_cors import CORS, cross_origin
import markdown.extensions.fenced_code

from DB.querys import (all_languages, is_language_exist, sentence_random, parse, sentence_by_id, search_sentence)
from Api.stats import send_report


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # set pretty print
app.config['JSON_AS_ASCII'] = False  # set unicode support for hebrew

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'  # set cors origin for the site


@cross_origin()
@app.route("/")
def home():
    """ home page """
    readme_file = open("Api/api-references.md", "r", encoding="UTF-8").read()
    md_template_string = markdown.markdown(
        readme_file, extensions=["fenced_code"]
    ).replace("\n", "<br/>")
    print(md_template_string)
    return render_template("docs.html", content=md_template_string)


@cross_origin()
@app.route("/language")
def languages():
    response = {"ok": True, "results": all_languages()}
    return response, 200


@cross_origin()
@app.route("/language/<language>")
def get_language(language):
    if is_language_exist(language):
        return {"ok": True}, 200
    return {"ok": True}, 404


@cross_origin()
@app.route("/sentence/random/")
def random_sentence():
    random_results = sentence_random(language=request.args.get("language"))
    response = [parse(sentence) for sentence in random_results]
    return {"ok": True, "results": response}, 200


@cross_origin()
@app.route("/sentence/<int:_id>")
def get_by_id(_id):
    data = parse(sentence_by_id(_id))
    return {"ok": True, "results": data}, 200 if data else {"ok": False}, 404


@cross_origin()
@app.route("/sentence/search")
def search():
    error = {}
    response = {}

    query = request.args.get("query") or request.args.get("q")
    limit = request.args.get("limit") or request.args.get("l") or 50  # set 50 for limit as default
    lang = request.args.get("language") or request.args.get("lang") or "ag"  # set language default to All languages

    # costume error
    if query == "make_error":
        return jsonify({"error": "costume error"})  # demo error for debugging

    if not query:
        error = {"error": "a `query` is required."}  # when `query` does not provided

    if lang and len(lang) != 2:
        error = {"error": "`language` must be two characters, e.g. `EN`."}  # wrong language format

    if limit and isinstance(limit, str) and not limit.isdigit():
        error = {"error": "`limit` must be a digit."}  # `limit` parameter does not number

    if error:
        return {"ok": False, "results": error}, 400

    with db_session:
        results = [parse(result) for result in search_sentence(
            query=query,
            limit=int(limit),
            lang=lang
        )]
        response["ok"] = True
        response["count"] = len(results)
        response["results"] = results

        return jsonify(response), 200


@cross_origin()
@app.route("/sentence/report", methods=['POST'])
def report():
    if request.method == 'POST':
        _id = request.form.get("id")
        if send_report(_id):
            return {"ok": True, "id": _id}, 200
        return {"ok": False}, 400
    return {"ok": False}, 405


if __name__ == '__main__':
    app.run()
