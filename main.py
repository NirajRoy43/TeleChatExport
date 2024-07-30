"""
© 2024 Niraj Roy. All rights reserved.

This file is part of the TeleChatExport project.

Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""


# main file
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, DeleteMessagesRequest
import logging

logging.basicConfig(level=logging.INFO)

api_id = input("Enter your API_ID: ")
api_hash = input("Enter your API_HASH: ")

# login script wala same session use karenge
client = TelegramClient('user_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='/save'))
async def handler(event):
    chat = event.chat_id
    sender = await event.get_sender()
    sender_id = sender.id

    # /save command delete krne ke liye
    await client(DeleteMessagesRequest(
        id=[event.message.id],
        revoke=True  
    ))

    # chat history nikal lenge
    all_messages = []
    offset_id = 0
    limit = 100  
    
    while True:
        history = await client(GetHistoryRequest(
            peer=chat,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))

        if not history.messages:
            break

        messages = history.messages
        for message in messages:
            all_messages.append(f"{message.sender_id}: {message.message}")

        offset_id = messages[-1].id

    # msg ko file me save kr lenge
    file_path = 'chat_export.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(all_messages))

    # file ko saved msg me bhej denge
    await client.send_file('me', file_path, caption=f"Extracted {len(all_messages)} messages from chat {chat}.")

client.start()
client.run_until_disconnected()
