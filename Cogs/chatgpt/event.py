import discord 
from discord.ext import  commands 
from discord.ui import * 
from ..checks import check
import openai


class on_chatgpt_message(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_message")
    @check.is_gpt_chan()
    async def on_message(self, message:discord.Message):
        completion=openai.Completion.create(engine="text-davinci-003",prompt=message,max_tokens=2000-len(message))
        await message.reply(completion.choice[0].text)