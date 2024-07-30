"""
© 2024 Niraj Roy. All rights reserved.

This file is part of the TeleChatExport project.

Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""

from telethon import TelegramClient
import logging


logging.basicConfig(level=logging.INFO)


api_id = input("Enter your API_ID: ")
api_hash = input("Enter your API_HASH: ")

if not api_id or not api_hash:
    raise ValueError("API_ID and API_HASH must be provided")

client = TelegramClient('user_session', api_id, api_hash)

async def main():
    await client.start()
    print("Client Created")
    me = await client.get_me()
    print(me.stringify())

with client:
    client.loop.run_until_complete(main())
