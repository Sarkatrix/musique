import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔧 Slash commands synchronisées ({len(synced)})")
    except Exception as e:
        print(f"Erreur lors de la sync : {e}")

@bot.tree.command(name="ping", description="Teste si le bot fonctionne")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong !")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if TOKEN is None:
        print("❌ DISCORD_TOKEN manquant")
    else:
        bot.run(TOKEN)
