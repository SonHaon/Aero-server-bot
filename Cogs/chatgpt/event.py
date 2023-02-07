import discord 
from discord.ext import  commands 
from discord.ui import * 
from ..checks import check
import openai


class on_chatgpt_message(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_message")
    async def on_message(self, message:discord.Message):
        if message.author.bot == False and message.channel.id == 1069338761772671158 :
            completion=openai.Completion.create(engine="text-davinci-003",prompt=message.content,max_tokens=2000-len(message.content))
            await message.reply(completion.choices[0].text)