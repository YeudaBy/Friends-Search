from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Bot.db import update_favorite, get_favorite_ids
from Bot.tools import lang_msg, get_sentence_msg, request_by_id


def get_btn_by_id(_id: int) -> InlineKeyboardButton:
    data = request_by_id(_id)
    return InlineKeyboardButton(
        data["content"], callback_data=f"kbf/{data['id']}"
    )


def show_favorites(_, callback: CallbackQuery):
    favorites = get_favorite_ids(callback.from_user.id)

    if not favorites:
        callback.answer(lang_msg(callback, "no_favorites"))
        return

    callback.answer("Will be added soon..")  # TODO show msg with favs

    keywords = InlineKeyboardMarkup([
        [get_btn_by_id(i), InlineKeyboardButton(
            "X", callback_data=f"rmf/{i}"
        )] for i in favorites
    ])

    # data = {favorites[i]: request_by_id(favorites[i])["content"] for i in range(len(favorites))}
    callback.edit_message_text("test to show favs", reply_markup=keywords)


def remove_favorite_from_list(_, callback: CallbackQuery):
    """ run at callback in format r"rmf/[0-9]*" """
    update_favorite(callback.from_user.id, int(callback.data.replace("rmf/", "")))
    callback.answer("Favorite was removed!")


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
    else:
        callback.answer(lang_msg(callback, 'only_sender_can_change'))
