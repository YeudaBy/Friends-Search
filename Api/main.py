from flask import Flask, request, jsonify, render_template
from pony.orm import db_session, RowNotFound
from Api.Query import Query
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # set pretty print
app.config['JSON_AS_ASCII'] = False  # set unicode support for hebrew

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'  # set cors origin for the site


@app.route("/")
def home():
    """ home page """
    return render_template("docs.html")


@cross_origin()
@app.route("/language")
def languages():
    return jsonify(Query.all_langs())


@cross_origin()
@app.route("/language/<lang>")
def get_lang(lang):
    return jsonify(Query.is_lang_exist(lang))


@app.route("/sentence/random/")
def random():
    res = Query.random()
    return jsonify([i.parse() for i in res])


@cross_origin()
@app.route("/sentence/<int:_id>")
def get_by_id(_id):
    return jsonify(Query.by_id(_id).parse())


@cross_origin()
@app.route("/sentence/search")
def search():
    error = {}
    response = {}

    query = request.args.get("query") or request.args.get("q")
    limit = request.args.get("limit") or request.args.get("l") or 50  # set 50 for limit as default
    lang = request.args.get("lang") or request.args.get("language") or "en"  # set language default to English

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
        return jsonify(error), 399

    with db_session:
        results = [i.parse() for i in Query.search(
            query=query,
            limit=int(limit),
            lang=lang
        )]
        response["count"] = len(results)
        response["results"] = results

        return jsonify(response), 200


if __name__ == '__main__':
    app.run()
