import discord
import os
from server import keep_alive
import commands

client = discord.Client()

@client.event
async def on_ready():
  global client
  print(f"{client.user} initialized")
  commands.client = client

prefix = "%c"

@client.event
async def on_message(message):
    if not commands.client:
      if message.author != client.user:
        # await message.channel.send("unintalized... please wait")
        pass
      return
    if prefix in message.content:
      await commands.getCommand(message)

keep_alive()
token = os.environ.get("BOT_TOKEN")
client.run(token)