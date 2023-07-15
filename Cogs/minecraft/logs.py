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
        if message.channel.id == 1050457771537080410 and (message.content.lower() == "log" or message.content.lower() == "logs"):
            if message.content.endswith("file"):
                await message.channel.send(file=discord.File(r"/home/sonhaon/minecraft/logs/latest.log"))
            else:
                with open("/home/sonhaon/minecraft/logs/latest.log","r",encoding="utf8") as file:
                    lines = file.readlines()
                lines.reverse()
                log=[]
                for i in range(100):
                    log.append(lines[i])
                    if "".join(log).count("") >= 2000:
                        log.pop()
                        break
                log.reverse()
                await message.channel.send(content=f"```{''.join(log)}```")    
            await message.delete()