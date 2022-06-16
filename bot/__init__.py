import os
from config import vars
from pyrogram import Client
from pyrogram.enums import ParseMode


app = Client(
    name=vars.client_name,
    api_id=vars.api_id,
    api_hash=vars.app_hash,
    bot_token=vars.bot_token,
    parse_mode=ParseMode.MARKDOWN,
    plugins=dict(root=os.path.join("bot", "plugs"))
    )