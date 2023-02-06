import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import random
import os
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging

class ping(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping",description="verifie si le bot marche")
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content="pong")
