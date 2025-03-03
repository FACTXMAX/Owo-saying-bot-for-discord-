import discord
import asyncio
import random

# Your bot token (keep this secret!)
TOKEN = "YOUR_BOT_TOKEN"

# Set up the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Define the target channel ID where the bot will send messages
CHANNEL_ID = 123456789012345678  # Replace with your channel ID

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Invalid channel ID. Make sure the bot has access.")
        return

    while True:
        await channel.send("owo random")
        delay = random.randint(10, 15)  # Wait 10-15 seconds
        await asyncio.sleep(delay)

# Run the bot
client.run(TOKEN)
