import re

from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, Message

from Bot.db import get_favorite_ids, get_lang, update_lang, create_user, update_favorite
from Bot.tools import lang_msg, lang_buttons, request_by_id, start_buttons, get_sentence_msg, change_lang_buttons, \
    report_on_id, random_img, request_by_sentence, get_sentence_result, close_msg_buttons


def ask_change_lang(_, callback: CallbackQuery):
    callback.edit_message_text(lang_msg(callback, "lang_chooser"), reply_markup=lang_buttons)


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


def close_msg(_, callback: CallbackQuery):
    callback.message.delete()


def edit_to(_, callback: CallbackQuery):
    create_user(user_id=callback.from_user.id, lang=callback.from_user.language_code)
    txt, kb = get_sentence_msg(int(callback.data), callback)
    callback.edit_message_text(txt)
    callback.edit_message_reply_markup(kb)


def ask_to_report(_, callback: CallbackQuery):
    create_user(user_id=callback.from_user.id, lang=callback.from_user.language_code)
    qid = int(callback.data.replace("r/", ""))
    callback.edit_message_text(
        lang_msg(callback, "ask_to_report"), reply_markup=change_lang_buttons(str(qid)))


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
