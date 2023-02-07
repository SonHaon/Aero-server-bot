import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *

class ping(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping",description="donne la latence du bot")
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content=f"le ping du bot est de {round(self.bot.latency*1000)}ms")
