from flask import request, jsonify
from flask_cors import cross_origin

from DB.querys import all_languages, is_language_exist, sentence_random, parse, sentence_by_id, search_sentence


@cross_origin()
def _languages():
    """ return dict of all languages supported """
    return {"ok": True, "results": all_languages()}, 200


@cross_origin()
def _get_language(language):
    """ return if language exists """
    response = is_language_exist(language)
    if response:
        return {"ok": True, "results": response}, 200
    return {"ok": True, "error": "language not found or noe supported yet"}, 404


@cross_origin()
def _random_sentence():
    """ return list of random sentences
     optional args: language [default=ag]
     """
    random_results = sentence_random(language=request.args.get("language"))
    response = [parse(sentence) for sentence in random_results]
    return {"ok": True, "results": response}, 200


@cross_origin()
def _get_by_id(_id):
    """ get the sentence by specific id """
    data = parse(sentence_by_id(_id))
    return ({"ok": True, "results": data}, 200) if data else (
        {"ok": False, "error": "sentence not found"}, 404)


@cross_origin()
def _search():
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
        error = {"error": "costume error"}  # demo error for debugging

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
