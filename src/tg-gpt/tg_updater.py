from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

API_ID = 26336592
API_HASH = "6cc551dde7f48bb0e9d5423c134a0aff"
PHONE = "+79151212711"
client = TelegramClient("session", API_ID, API_HASH)

async def tg_update():
    await client.start()
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(dialog.title)
 #       chat = await client.get_entity(dialog.title)
#        async for message in client.iter_messages(chat):
#            print(f"Message ID: {message.id}, Date: {message.date}, From: {message.sender_id}, Text: {message.text}")