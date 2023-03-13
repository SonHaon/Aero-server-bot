import discord
from discord.ui import view,Button,Select,Modal
from discord import app_commands,ButtonStyle


class boutons_auto_role(discord.ui.View):
    def __init__(self,guild:discord.Guild):
        super().__init__(timeout=None)
    
    
    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:rouge:1084924751954329660>",
        custom_id="rouge",
        row=1
    )
    async def infini(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:vert:1084924793016565830>",
        custom_id="vert",
        row=1
    )
    async def alors(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:violet:1084924636971675791>",
        custom_id="violet",
        row=1
    )
    async def alors(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

  