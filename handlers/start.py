from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}! Hii
I am powerful VC music Bot..🔥
I can play songs in your group's VC..😉

My owner :-× @SEDxD

And don't forgot to promote me with all rights..😉
Otherwise I can't play songs..🙄

Use the buttons below to know more about me..🔥
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MY CREATOR", url="https://t.me/SEDXD",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "SUPPORT GROUP", url="https://t.me/X_F0RCE_TEAM"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/X_F0RCED"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Commands", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Munna_vc_robot?startgroup=true"
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
