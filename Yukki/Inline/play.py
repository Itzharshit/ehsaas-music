from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def url_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            
            InlineKeyboardButton(
                text="โฐ๐๐ช๐จ๐๐ ๐๐ก๐๐ฎโฑ",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="โฐ๐๐๐๐๐ค ๐๐ก๐๐ฎโฑ",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
            
        ],
        [
            InlineKeyboardButton(
                text="โฐ๐๐ง๐ค๐ช๐ฅโฑ",
                url=f"https://t.me/World_friends_chatting_group",
            ),
            InlineKeyboardButton(
                text="โฐ๐๐ฌ๐ฃ๐๐งโฑ",
                url=f"https://t.me/ARMY0071",
            ),
        ],
    ]
    return buttons


def url_markup2(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="โฐ๐๐ช๐จ๐๐ ๐๐ก๐๐ฎโฑ",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="โฐ๐๐๐๐๐ค ๐๐ก๐๐ฎโฑ",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="โฐ๐ ๐๐น๐ผ๐๐ฒโฑ",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="1๏ธโฃ", callback_data=f"Yukki {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="2๏ธโฃ", callback_data=f"Yukki {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="3๏ธโฃ", callback_data=f"Yukki {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="4๏ธโฃ", callback_data=f"Yukki {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="5๏ธโฃ", callback_data=f"Yukki {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="โฐ๐ ๐๐น๐ผ๐๐ฒโฑ", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="6๏ธโฃ",
                callback_data=f"Yukki {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="7๏ธโฃ",
                callback_data=f"Yukki {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="8๏ธโฃ",
                callback_data=f"Yukki {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="9๏ธโฃ",
                callback_data=f"Yukki {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="๐",
                callback_data=f"Yukki {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="โฐ๐ ๐๐น๐ผ๐๐ฒโฑ", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def secondary_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="โฐ๐๐ฌ๐ฃ๐๐งโฑ", url=f"https://t.me/ARMY0071"
            ),
            InlineKeyboardButton(text="โฐ๐๐ง๐ค๐ช๐ฅโฑ", url=f"https://t.me/World_friends_chatting_group"),
        ],
    ]
    return buttons


def secondary_markup2(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="โฐ๐ ๐๐น๐ผ๐๐ฒโฑ", callback_data=f"close"),
        ],
    ]
    return buttons


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text="โฐ๐๐ฌ๐ฃ๐๐งโฑ", url=f"https://t.me/ARMY0071"
            ),
            InlineKeyboardButton(text="โฐ๐๐ง๐ค๐ช๐ฅโฑ", url=f"https://t.me/World_friends_chatting_group"),
        ],
    ]
    return buttons


def timer_markup(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text="โฐ๐๐ฌ๐ฃ๐๐งโฑ", url=f"https://t.me/ARMY0071"
            ),
            InlineKeyboardButton(text="โฐ๐๐ง๐ค๐ช๐ฅโฑ", url=f"https://t.me/World_friends_chatting_group"),
        ],
    ]
    return buttons


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [InlineKeyboardButton(text="โฐ๐ ๐๐น๐ผ๐๐ฒโฑ", callback_data=f"close")],
    ]
    return buttons


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    buttons = [
        [InlineKeyboardButton(text="โฐ๐ ๐๐น๐ผ๐๐ฒโฑ", callback_data=f"close")],
    ]
    return buttons


audio_markup2 = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("โฐ๐ ๐๐น๐ผ๐๐ฒโฑ", callback_data="close")],
    ]
)
