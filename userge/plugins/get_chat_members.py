"""This example shows how to get all the members of a chat."""

from pyrogram import Client
from datetime import datetime
from userge import userge, Message


@userge.on_cmd("/users", about={'header': "Где ж ты?"})
async def app = Client("my_account")
target = "LOG_CHANNEL_ID"  # Target channel/supergroup

with app:
    for member in app.iter_chat_members(target):
        print(member.user.first_name)
