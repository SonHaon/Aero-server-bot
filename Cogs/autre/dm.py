import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *

from ..checks import check

class dm(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="dm",description="envoie un mp de la part du bot")
    @check.is_SonHaon()
    async def dm(self,interaction:discord.Interaction,user:discord.User,message:str):
        await interaction.response.defer(ephemeral=True)
        try:
            await user.send(message)
            await interaction.edit_original_response(content=f"j'ai bien envoyé `{message}` à {user.mention}")
        except:
            await interaction.edit_original_response(content=f"je n'ai pas pu envoyé de message à {user.mention}, soit nous n'avons pas de server en commun soit il n'accepte pas les messages privés")
