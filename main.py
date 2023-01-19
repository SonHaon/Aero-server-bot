import asyncio
from pathlib import Path
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import random
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging
import logging.handlers
import spam

TOKEN = "MTA1MDQ1NTMxOTMzNzI0Njc0MA.GgJBO2.Pj6EyPJFbKzq7gOfbCUsAZNRn3QSx8mgsRp-50"
guild = discord.Object(id=1022844623372165260)




class aclient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents,command_prefix="%µ¨£%£µ%",help_command=None)
        
    async def setup_hook(self):
        # commandes normal
        await self.add_cog(spam.spam(bot=self),guild=guild)
        await self.tree.sync(guild=guild)


    async def on_ready(self):
        await self.wait_until_ready()
        print("ready")

SonHaon_Bot = aclient()
tree = SonHaon_Bot.tree




SonHaon_Bot.run(TOKEN)