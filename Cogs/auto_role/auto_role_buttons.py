import discord
from discord.ui import view,Button,Select,Modal
from discord import app_commands,ButtonStyle



class boutons_auto_role(discord.ui.View):
    def __init__(self,guild:discord.Guild):
        super().__init__(timeout=None)
        self.role_couleur=[guild.get_role(1084920603301126236), #bleu
                           guild.get_role(1084920648268263566), #jaune
                           guild.get_role(1084920682766409758), #orange
                           guild.get_role(1084920165554213054), #rose
                           guild.get_role(1084920710134243450), #rouge
                           guild.get_role(1084920738953302107), #vert
                           guild.get_role(1084920504978264095), #violet
                           guild.get_role(1084929663710797925), #marron
                          ]
    
    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:bleu:1084924665954324491>",
        custom_id="1",
        row=0
    )
    async def bleu(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920603301126236)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur bleu vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:jaune:1084924695838736404>",
        custom_id="2",
        row=0
    )
    async def jaune(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920648268263566)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur jaune vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:orange:1084924723756027936>",
        custom_id="3",
        row=0
    )
    async def orange(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920682766409758)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur orange vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:rose:1084924591274741771>",
        custom_id="4",
        row=0
    )
    async def rose(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920165554213054)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur rose vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:rouge:1084924751954329660>",
        custom_id="5",
        row=1
    )
    async def rouge(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920710134243450)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur rouge vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:vert:1084924793016565830>",
        custom_id="6",
        row=1
    )
    async def vert(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920738953302107)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur vert vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:violet:1084924636971675791>",
        custom_id="7",
        row=1
    )
    async def violet(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084920504978264095)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur violet vous a été donné",ephemeral=True)

    @discord.ui.button(
        style=ButtonStyle.grey,
        emoji="<:marron:1084929867985989703>",
        custom_id="8",
        row=1
    )
    async def marron(self,interaction:discord.Interaction,button:discord.ui.Button):
        for role in interaction.user.roles:
            if role in self.role_couleur:
                await interaction.user.remove_roles(role)
        role = interaction.guild.get_role(1084929663710797925)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"la couleur marron vous a été donné",ephemeral=True)