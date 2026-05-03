import discord
from discord.ext import commands
import os

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# CONFIGURATION - YOU NEED TO SET THESE
INTRO_CHANNEL_NAME = "✏️┊introductions"  # Your intro channel name
VERIFIED_ROLE_NAME = "Verified✅"         # Role to give (change to "Verified" if needed)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')
    print(f'📋 Watching for messages in #{INTRO_CHANNEL_NAME}')
    print(f'🎯 Will give role: {VERIFIED_ROLE_NAME}')

@bot.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return
    
    # Check if message is in introductions channel
    if message.channel.name == INTRO_CHANNEL_NAME:
        guild = message.guild
        member = message.author
        
        # Find the verified role
        verified_role = discord.utils.get(guild.roles, name=VERIFIED_ROLE_NAME)
        
        if not verified_role:
            print(f'❌ ERROR: Role "{VERIFIED_ROLE_NAME}" not found!')
            print(f'   Create this role in your server first!')
            return
        
        # Check if user already has the role
        if verified_role in member.roles:
            print(f'ℹ️  {member.name} already has {VERIFIED_ROLE_NAME} role')
            return
        
        # Give the role
        try:
            await member.add_roles(verified_role)
            print(f'✅ Gave {VERIFIED_ROLE_NAME} role to {member.name}')
            
            # Optional: Send a welcome message
            await message.channel.send(
                f'Welcome {member.mention}! You now have access to the server! 🎉'
            )
        except discord.Forbidden:
            print(f'❌ ERROR: Bot doesn\'t have permission to assign roles!')
            print(f'   Make sure bot role is ABOVE {VERIFIED_ROLE_NAME} in role hierarchy')
        except Exception as e:
            print(f'❌ ERROR: {e}')

# Run the bot
if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    
    if not TOKEN:
        print('❌ ERROR: No bot token found!')
        print('   Set DISCORD_BOT_TOKEN environment variable')
        print('   OR paste your token below:')
        TOKEN = input('Enter bot token: ').strip()
    
    if TOKEN:
        print('🚀 Starting bot...')
        bot.run(TOKEN)
    else:
        print('❌ No token provided. Exiting.')
