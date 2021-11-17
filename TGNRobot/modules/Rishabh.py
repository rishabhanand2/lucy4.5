import tgEasy
from tgEasy import tgClient
from pyrogram import Client

app = tgClient(Client('my_account'))

@app.command("rishabh")
async def start(client, message):
    await message.reply_text("Hello")



