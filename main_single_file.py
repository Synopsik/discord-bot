import discord
import os
from dotenv import load_dotenv
load_dotenv()

# Create intents item with default configuration
# Then modify attributes for permissions we need
intents = discord.Intents.default()
intents.presences = True # Allows the bot to view user presence (e.g., online/offline status)
intents.members = True # Lets the bot access member-related data (e.g., when users join or leave the server)
intents.message_content = True # Gives the bot access to read message content, such as the text within a message

# Create client bot instance
client = discord.Client(intents=intents)

# Setup token from environment,
# Alternatively this can be hardcoded
# token = "t0k3n...akljS2"
token = os.getenv("BOT_TOKEN")

@client.event
async def on_ready():
    # Once our bot is loaded the on_ready event is called
    print(f"Logged in as {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message):
    # If the message the bot is viewing was written by the bot,
    # break out of function on_message
    if message.author == client.user:
        return
    # Begin case statement to search for bot commands
    match message.content:
        case "!ping":
            await message.channel.send("Pong!")
            print(f"[COMMAND] {message.author} sent command {message.content}")
            # To reply directly we can do this instead
            # await message.channel.reply("Pong!")
        case _:
            # Default case, print to console
            print(f"[MESSAGE] {message.author}: {message.content}")

# Run our bot once it is configured
client.run(token)