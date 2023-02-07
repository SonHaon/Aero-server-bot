import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import openai
from ..checks import check

openai.api_key = "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"

class chatgpt(commands.GroupCog, name="chatgpt"): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        super().__init__()

    @app_commands.command(name="ask",description="pose une question a chatgpt")
    @check.is_gpt_chan()
    async def ask(self, interaction:discord.Interaction,question:str):
        await interaction.response.defer(ephemeral=False)
        completion=openai.Completion.create(engine="text-davinci-003",prompt=question,max_tokens=2000)
        await interaction.edit_original_response(content=completion.choices[0].text)

    @ask.error
    async def on_error(self, interaction:discord.Interaction, error):
        if isinstance(error,app_commands.CheckFailure):
            await interaction.response.send_message("Vous ne pouvez pas faire ca ici, \nil faut aller dans <#1069338761772671158>")

