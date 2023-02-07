import discord
from discord.ext import commands
from discord.ui import *
import os
from dotenv import load_dotenv
from Cogs_sommaire import *

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")
guild = discord.Object(id=1022844623372165260)




class aclient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents,command_prefix="%µ¨£%£µ%",help_command=None)
        
    async def setup_hook(self):
        # commandes normal :
        await self.add_cog(ping(bot=self),guild=guild)

        # commandes bot :
        await self.add_cog(reboot(bot=self),guild=guild)

        # commandes chatgpt :


        # commandes minecraft :
        await self.add_cog(mc_commands(bot=self),guild=guild)
        await self.add_cog(logs(bot=self),guild=guild)
        await self.add_cog(start_mc(bot=self),guild=guild)
        await self.tree.sync(guild=guild)

        # commandes moderation :
        await self.add_cog(clear(bot=self),guild=guild)

        # commandes troll :
        await self.add_cog(spam(bot=self),guild=guild)


    async def on_ready(self):
        await self.wait_until_ready()
        print("ready")

bot = aclient()


bot.run(TOKEN)