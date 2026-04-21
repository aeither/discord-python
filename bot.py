import discord
import os
from discord.ext import tasks

TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = 625247884794658816          # ID de ton serveur
CHANNEL_ID = 905508012440027186       # ID du salon où poster
ROLE_IDS = [979059050635485225, 905508354816897065, 979059317774901349, 979059113428414525, 905508238823391332, 979059197553573929]   # IDs des rôles à lister

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connecté : {client.user}")
    if not weekly_post.is_running():
        weekly_post.start()

@tasks.loop(hours=168)
async def weekly_post():
    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("❌ Serveur introuvable, vérifie GUILD_ID")
        return

    channel = guild.get_channel(CHANNEL_ID)
    if not channel:
        print("❌ Salon introuvable, vérifie CHANNEL_ID")
        return

    await channel.send("📋 **Liste hebdomadaire des membres**")

    for role_id in ROLE_IDS:
        role = guild.get_role(role_id)
        if not role:
            print(f"❌ Rôle {role_id} introuvable, ignoré")
            continue
        members = [m.display_name for m in role.members]
        message = f"**{role.name}** ({len(members)}) :\n"
        message += "\n".join(f"• {m}" for m in members)
        await channel.send(message)

client.run(TOKEN)
