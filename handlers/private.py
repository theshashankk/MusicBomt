from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am powerful bot of VC music Bot..😁🔥
To play music also add

@danishbabamusic to your Telegram Group..😉.

Use the buttons below to know more about me..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "🎛️ Music World 🎛️", url="https://t.me/wearefriendscircle"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "My CREATOR ☺️", url="https://t.me/idanishbaba"
                    ),
                    InlineKeyboardButton(
                        "Add Me To Group", url="https://t.me/danishbabamusic_bot?startgroup=true"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
