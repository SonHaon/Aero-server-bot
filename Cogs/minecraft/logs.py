import discord 
from discord.ext import  commands 
from discord.ui import * 
from ..checks import check
import openai


class logs(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_message")
    async def logs(self, message:discord.Message):
        if message.channel.id == 1050457771537080410 and message.content.lower() == "log" or message.content.lower() == "logs":
            message.channel.send(file=discord.File(r"/home/sonhaon/minecraft/logs/latest.log"))
            