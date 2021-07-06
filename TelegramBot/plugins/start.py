from .. import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/start$'))
async def start(event):
    await event.reply("Heya 🙋🏻.")

