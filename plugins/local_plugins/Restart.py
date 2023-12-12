import re, asyncio, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import ADMINS

    
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**⎋ 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐬 𝐒𝐭𝐨𝐩𝐞𝐝 𝐁𝐨𝐭 𝐢𝐬 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠◐◐◐**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**√ 𝐁𝐨𝐭 𝐢𝐬 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝.𝐍𝐨𝐰 𝐲𝐨𝐮 𝐂𝐚𝐧 𝐔𝐬𝐞 𝐦𝐞**")
    os.execl(sys.executable, sys.executable, *sys.argv)
