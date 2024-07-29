# Login krne ke liye
from telethon import TelegramClient
import logging

logging.basicConfig(level=logging.INFO)

# apna value dalo bhai
api_id = 'API_ID'
api_hash = 'API_HASH'

client = TelegramClient('user_session', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created")
    me = await client.get_me()
    print(me.stringify())

with client:
    client.loop.run_until_complete(main())