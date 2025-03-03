import discord
import asyncio
import random

# Ask for Bot Token and Channel ID
TOKEN = input("Enter your Discord Bot Token: ").strip()
CHANNEL_ID = int(input("Enter the Channel ID: ").strip())

# Set up Discord bot with necessary intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

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
