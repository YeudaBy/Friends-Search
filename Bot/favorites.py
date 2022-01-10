from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Bot.db import update_favorite, get_favorite_ids
from Bot.tools import lang_msg, get_sentence_msg, request_by_id


def get_btn_by_id(_id: int) -> InlineKeyboardButton:
    data = request_by_id(_id)
    return InlineKeyboardButton(
        data["content"], callback_data=str(data['id'])
    )


def favorites_keyboard(favorites: list) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [get_btn_by_id(i), InlineKeyboardButton(
            "❌", callback_data=f"rf/{i}"
        )] for i in favorites
    ])


def show_favorites(_, callback: CallbackQuery):
    favorites = get_favorite_ids(callback.from_user.id)
    if not favorites:
        callback.answer(lang_msg(callback, "no_favorites"))
        return
    callback.edit_message_text(lang_msg(callback, "list_of_favorites"), reply_markup=favorites_keyboard(favorites))


def remove_favorite_from_list(_, callback: CallbackQuery):
    update_favorite(callback.from_user.id, int(callback.data.replace("rf/", "")))
    if not get_favorite_ids(callback.from_user.id):
        callback.answer(lang_msg(callback, "no_more_favs"))
        callback.message.delete()
        return
    show_favorites(_, callback)


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
