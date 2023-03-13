import discord
from discord.ui import view,Button,Select,Modal
from discord import app_commands,ButtonStyle


class boutons_auto_role(discord.ui.View):
    def __init__(self,guild:discord.Guild):
        super().__init__(timeout=None)
    
    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:bleu:1084924665954324491>",
        custom_id="bleu",
        row=0
    )
    async def duo(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:jaune:1084924695838736404>",
        custom_id="jaune",
        row=0
    )
    async def duel(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:orange:1084924723756027936>",
        custom_id="orange",
        row=0
    )
    async def ios(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:rose:1084924591274741771>",
        custom_id="rose",
        row=0
    )
    async def android(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass

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

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="Voir mes roles",
        custom_id="voir_role",
        row=2
    )
    async def view_role(self,interaction:discord.Interaction,button:discord.ui.Button):
        user=interaction.user
        virgule = ", "
        roles = []
        for role in user.roles:
            roles.append(role.mention)
        roles.reverse()
        await interaction.response.send_message(f"vous avez les roles suivant : {virgule.join(roles)}",ephemeral=True)