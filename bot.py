from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # Required for member-related events
intents.message_content = True  # Enables the message content intent

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("Bot Ready To Use!")
    print("-----------------")


@client.command()
async def hello(ctx):
    await ctx.send("مرحبا بعضو طاقمي المذهل ! رارارارارارا! ")

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError("No token found. Make sure DISCORD_TOKEN is set in your environment variables.")
    bot.run(token)
