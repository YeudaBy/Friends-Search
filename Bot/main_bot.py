from pyrogram import Client, filters
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
                            CallbackQuery)
from pyrogram.errors import MessageNotModified
from Bot.db import edit_favorite, create_user, get_favorites
from Bot.tools import lang_msg, request_by_sentence, request_by_id, get_sentence_msg, get_sentence_result, \
    random_img
from os import getenv
from dotenv import load_dotenv

load_dotenv()
app = Client(
    "FriendSearch",
    api_id=int(getenv("API_ID")),
    api_hash=getenv("API_HASH"),
    bot_token=getenv("MAIN_TOKEN")
)


@app.on_message(filters.command(["start", "help", "translate", "history"]) & filters.private)
def start(_, message: Message):
    create_user(user_id=message.from_user.id, lang=message.from_user.language_code)
    if message.command == ["start"]:
        message.reply(lang_msg(message, "start_msg").format(message.from_user.mention))
    elif message.command == ["history"]:
        ids = get_favorites(user_id=message.from_user.id)
        search_history = []
        for _id in ids:
            search_history.append(request_by_id(_id))
        message.reply(lang_msg(message, "history".format(search_history)))
    elif message.command == ["help"]:
        message.reply(lang_msg(message, "help_msg"))
    elif message.command == ["translate"]:
        message.reply(lang_msg(message, "translate_msg"))


@app.on_inline_query(~filters.regex(r"\d"))
def search_inline(_, query: InlineQuery):
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
                 switch_pm_parameter="count"
                 )


# favorites button
@app.on_callback_query(filters.regex(r"f/\d"))
def favorites(_, callback: CallbackQuery):
    qid = int(callback.data.replace("f/", ""))
    # if callback.message.from_user == callback.from_user:
    if edit_favorite(callback.from_user.id, qid):
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


@app.on_callback_query(filters.regex(r"\d"))
def edit_to(_, callback: CallbackQuery):
    txt, kb = get_sentence_msg(int(callback.data), callback)
    callback.edit_message_text(txt)
    callback.edit_message_reply_markup(kb)


@app.on_inline_query(filters.regex(r"\d"))
def search_by_id(_, inline: InlineQuery):
    inline.answer([InlineQueryResultArticle(
        title="Click here to share your sentence!",
        description=f"{request_by_id(int(inline.query))['content']}",
        thumb_url=random_img(),
        input_message_content=InputTextMessageContent(
            message_text=get_sentence_msg(int(inline.query), inline)[0]
        ),
        reply_markup=get_sentence_msg(int(inline.query), inline)[1]
    )])


app.run()
