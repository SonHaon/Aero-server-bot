import discord 
from discord.ext import  commands 
from discord import  app_commands
from discord.ui import * 
import os
from ..checks import check

class raspberry(commands.GroupCog, name="raspberry"): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        super().__init__()

    @app_commands.command(name="terminal",description="execute une commande sur le terminal linux")
    @check.is_SonHaon()
    async def commands(self, interaction:discord.Interaction, commande:str):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content=f"```sonhaon@raspberrypi:/$ {commande}\n{os.popen(commande).read()}```")


#    @app_commands.command(name="start",description="lance le serveur minecraft")
#    @check.is_modo()
#    async def start_mc(self, interaction:discord.Interaction):
#        await interaction.response.defer(ephemeral=True)
#        os.system(f'sudo systemctl start minecraft')
#        await interaction.edit_original_response(content=f"le server démarre")