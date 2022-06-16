from bot import app
from config import vars
from pyrogram import filters


@app.on_message(filters.text & filters.command(["start"]))
async def _start(_client, message):
    await message.reply("I'm alive!")