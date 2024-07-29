
from telethon import TelegramClient
import logging
import os

logging.basicConfig(level=logging.INFO)


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('user_session', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created")
    me = await client.get_me()
    print(me.stringify())

with client:
    client.loop.run_until_complete(main())
