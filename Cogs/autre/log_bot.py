import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import os

from ..checks import check

class log_bot(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="log_bot",description="fait des test")
    @check.is_SonHaon()
    async def log_bot(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        message=os.popen("pwd").read()
        await interaction.edit_original_response(content=message)
