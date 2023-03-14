import discord
from discord.ui import view,Button,Select,Modal
from discord import app_commands,ButtonStyle


class boutons_auto_role(discord.ui.View):
    def __init__(self,guild:discord.Guild):
        super().__init__(timeout=None)
    
    
    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:vert:1084924793016565830>",
        custom_id="6",
        row=1
    )
    async def alors(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:violet:1084924636971675791>",
        custom_id="7",
        row=1
    )
    async def alors(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass