import re

from pyrogram import Client, filters
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
                            CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.errors import MessageNotModified
from Bot.db import update_favorite, create_user, get_favorites, update_lang, get_lang
from Bot.tools import lang_msg, request_by_sentence, request_by_id, get_sentence_msg, get_sentence_result, \
    random_img, report_on_id, start_buttons, lang_buttons, change_lang_buttons, close_msg_buttons
from os import getenv
from dotenv import load_dotenv

load_dotenv()
app = Client(
    "FriendSearch",
    api_id=int(getenv("API_ID")),
    api_hash=getenv("API_HASH"),
    bot_token=getenv("MAIN_TOKEN")
)


@app.on_message(filters.regex(r"^/.*") & filters.private)
def show_msg(_, message: Message):
    create_user(user_id=message.from_user.id, lang=message.from_user.language_code)
    if message.text == "/start":
        message.reply(lang_msg(message, "start_msg").format(message.from_user.mention),
                      reply_markup=start_buttons(message))
    elif message.text in ["favorites", "/favs"]:
        message.reply("Will be added soon..")  # TODO show favs list
    elif message.text in ["/about", "/ab"]:
        message.reply(lang_msg(message, "about_msg"), reply_markup=close_msg_buttons)
    elif message.text in ["/translate", "/tr"]:
        message.reply(lang_msg(message, "translate_msg"), reply_markup=close_msg_buttons)
    elif message.text in ["/change_lang", "/lang", "/cl"]:
        message.reply(lang_msg(message, "lang_chooser"), reply_markup=lang_buttons)
    else:
        message.reply(lang_msg(message, "no_command"), reply_markup=close_msg_buttons)


@app.on_inline_query(~filters.regex(r"\d"))
def search_inline(_, query: InlineQuery):
    create_user(user_id=query.from_user.id, lang=query.from_user.language_code)
    raw_results = request_by_sentence(query.query)

    # errors handler
    if raw_results.get("error") or raw_results["count"] == 0:
        query.answer(
            results=[],
            switch_pm_text=lang_msg(query, 'query_required' if raw_results.get("error") else 'no_results'),
            switch_pm_parameter="empty"
        )
        return

    results = [get_sentence_result(result["id"], query) for result in raw_results["results"] if result['id']]
    query.answer(results,
                 cache_time=0,  # TODO remove
                 switch_pm_text=f"{lang_msg(query, 'results_count')}: {str(raw_results['count'])}",
                 switch_pm_parameter="count")


# favorites button
@app.on_callback_query(filters.regex(r"f/\d"))
def edit_favorites(_, callback: CallbackQuery):
    qid = int(callback.data.replace("f/", ""))
    # if callback.message.from_user == callback.from_user:
    if update_favorite(callback.from_user.id, qid):
        callback.answer(lang_msg(callback, 'added_to_fav'))
    else:
        callback.answer(lang_msg(callback, 'remove_from_fav'))
    try:
        callback.edit_message_reply_markup(
            get_sentence_msg(qid, callback)[1]
        )
    except MessageNotModified:
        pass
    # else:
    #     callback.answer(lang_msg(callback, 'only_sender_can_change'))


# report button
@app.on_callback_query(filters.regex(r"r/\d"))
def ask_to_report(_, callback: CallbackQuery):
    create_user(user_id=callback.from_user.id, lang=callback.from_user.language_code)
    qid = int(callback.data.replace("r/", ""))
    callback.edit_message_text(
        lang_msg(callback, "ask_to_report"), reply_markup=change_lang_buttons(str(qid)))


# handle report
@app.on_callback_query(filters.regex(r"(y|n)/\d"))
def report(_, callback: CallbackQuery):
    create_user(user_id=callback.from_user.id, lang=callback.from_user.language_code)
    qid = int(re.sub("[y, n]/", "", callback.data))
    if callback.data == f"y/{qid}":
        if report_on_id(qid)["status"] == "ok":
            callback.answer(lang_msg(callback, 'reported'))
    else:
        callback.answer(lang_msg(callback, 'not_reported'))
    txt, kb = get_sentence_msg(qid, callback)
    callback.edit_message_text(txt)
    callback.edit_message_reply_markup(kb)


@app.on_callback_query(filters.regex(r"\d"))
def edit_to(_, callback: CallbackQuery):
    create_user(user_id=callback.from_user.id, lang=callback.from_user.language_code)
    txt, kb = get_sentence_msg(int(callback.data), callback)
    callback.edit_message_text(txt)
    callback.edit_message_reply_markup(kb)


@app.on_inline_query(filters.regex(r"\d"))
def search_by_id(_, inline: InlineQuery):
    create_user(user_id=inline.from_user.id, lang=inline.from_user.language_code)
    inline.answer([InlineQueryResultArticle(
        title="Click here to share your sentence!",
        description=f"{request_by_id(int(inline.query))['content']}",
        thumb_url=random_img(),
        input_message_content=InputTextMessageContent(
            message_text=get_sentence_msg(int(inline.query), inline)[0]
        ),
        reply_markup=get_sentence_msg(int(inline.query), inline)[1]
    )])


@app.on_callback_query(filters.regex("change_lang"))
def ask_change_lang(_, callback: CallbackQuery):
    callback.edit_message_text(lang_msg(callback, "lang_chooser"), reply_markup=lang_buttons)


@app.on_callback_query(filters.regex(r"l/[a-z]+"))
def change_language(_, callback: CallbackQuery):
    create_user(user_id=callback.from_user.id, lang=callback.from_user.language_code)
    new_lang = callback.data.replace("l/", "")
    if new_lang == get_lang(callback.from_user.id):
        callback.answer(lang_msg(callback, "same_lang"))
    elif new_lang == "close":
        callback.edit_message_text(lang_msg(callback, "start_msg").format(callback.from_user.mention),
                                   reply_markup=start_buttons(callback))
    else:
        update_lang(callback.from_user.id, new_lang)
        callback.answer(lang_msg(callback, "lang_updated"))
        callback.edit_message_text(lang_msg(callback, "start_msg").format(callback.from_user.mention),
                                   reply_markup=start_buttons(callback))


@app.on_callback_query(filters.regex("favs"))
def show_favorites(_, callback: CallbackQuery):
    favorites = get_favorites(callback.from_user.id)
    if favorites:
        callback.answer("Will be added soon..")  # TODO show msg with favs
    else:
        callback.answer(lang_msg(callback, "no_favorites"))


@app.on_callback_query(filters.regex("close_msg"))
def close_msg(_, callback: CallbackQuery):
    callback.message.delete()


app.run()
