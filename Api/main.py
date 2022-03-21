import datetime
import time

from flask import Flask, request, jsonify, redirect
from flask_cors import CORS, cross_origin
from pony.flask import Pony

from Api.post import verify_sentence, report_sentence, review_content, _like_sentence
from Api.get import _languages, _get_language, _random_sentence, _get_by_id, _search
from Api.utils import AppConfig
from DB.db import Usage
from DB.querys import (all_languages, is_language_exist, sentence_random, parse, sentence_by_id, search_sentence,
                       like_sentence, get_usages_of_methode)

# -------- Flask initialization ----------
app = Flask(__name__)
Pony(app)

# --------- CORS configuration ----------
cors = CORS(app)

# ----- App configuration -------
app.config.from_object(AppConfig)


# ------ Statistics --------
@app.before_request
def _save_usage():
    Usage(uri=request.path, time=datetime.datetime.now(), user_agent=request.user_agent.__dict__)


# ------ Docs --------
@cross_origin()
@app.route("/docs")
def home():
    """ home page """
    return redirect("https://friends-search.readthedocs.io/")


# -------- GET methods ----------
# === languages ===
app.add_url_rule(rule="/language", view_func=_languages)
app.add_url_rule(rule="/language/<language>", view_func=_get_language)
# === sentences ===
app.add_url_rule(rule="/sentence/<int:_id>", view_func=_get_by_id)
app.add_url_rule(rule="/sentence/random/", view_func=_random_sentence)
app.add_url_rule(rule="/sentence/search", view_func=_search)
# === statistics ===

# ------ POST methods -------
# === admin ===
app.add_url_rule(rule="/sentence/<int:_id>/verify", view_func=verify_sentence, methods=["POST"])
app.add_url_rule(rule="/sentence/<int:_id>/review", view_func=review_content, methods=["POST"])
# === details ===
app.add_url_rule(rule="/sentence/<int:_id>/like", methods=['POST'], view_func=_like_sentence)
app.add_url_rule(rule="/sentence/<int:_id>/report", methods=["POST"], view_func=report_sentence)


if __name__ == '__main__':
    app.run()
