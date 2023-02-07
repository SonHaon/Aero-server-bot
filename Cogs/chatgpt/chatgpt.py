import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import openai

openai.api_key = "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"

class chatgpt(commands.GroupCog, name="chatgpt"): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        super().__init__()

    @app_commands.command(name="ask",description="pose une question a chatgpt")
    async def ask(self, interaction:discord.Interaction,question:str):
        await interaction.response.defer(ephemeral=True)
        completion=openai.Completion.create(engine="ada",prompt=question)
        await interaction.edit_original_response(content=completion.choices[0].text)
