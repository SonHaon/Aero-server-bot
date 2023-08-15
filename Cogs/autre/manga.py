import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
from requests import get
from scrapy import Selector
import os
import shutil
import os

def file_create(manga,chap):
    try:
        os.mkdir("img")
    except:
        pass
    try:
        os.mkdir(f"img/{manga}")
    except:
        pass
    try:
        os.mkdir(f"img/{manga}/{chap}")
    except:
        pass
    try:
        os.mkdir(f"cbz")
    except:
        pass
    try:
        os.mkdir(f"cbz/{manga}")
    except:
        pass

def scrap(manga,chap):
    for i in range(100):
        if i !=0:
            reponse = get(url=f"https://lelscanvf.cc/manga/{manga}/{chap}/{i}")
            if reponse.status_code == 404:
                print("manga introuvable")
                break
            source = reponse.text
            selector = Selector(text=source)
            images= selector.css("img").xpath("@src")
            for image in images:
                name: str = image.extract()
                if name.find(chap)!=-1:
                    name=f"https://{name.removeprefix(' //').removesuffix('g ')}g"
                    test=get(name)
                    if test.status_code!=200:
                        print("image marche pas", test.status_code)
                        return
                    with open(f"img/{manga}/{chap}/{i}.jpg","wb") as f:
                        f.write(test.content)
            if len(images) ==1:
                return        

def compresse(manga,chap):
    shutil.make_archive(f"img/{manga}/{chap}","zip",f"img/{manga}/{chap}")
    try:
        os.remove(f"cbz/{manga}/{chap}.cbz")
    except:
        pass
    os.rename(f"img/{manga}/{chap}.zip",f"cbz/{manga}/{chap}.cbz")

def supprime():
    shutil.rmtree("img")
    shutil.rmtree("cbz")


class manga(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    
    @app_commands.command(name="manga_scan",description="envoie un fichier du chapitre du manga voulu")
    @app_commands.choices(manga= [
        app_commands.Choice(name=f"One Piece",value="one-piece"),
        app_commands.Choice(name="Naruto",value="naruto"),
        app_commands.Choice(name="Dragon ball Super",value="dragon-ball-super"),
        app_commands.Choice(name="My Hero Academia",value="my-hero-academia")
    ])
    async def manga(self,interaction:discord.Interaction,manga:str,chapitre:str):
        await interaction.response.defer(ephemeral=True)
        file_create(manga,chapitre)
        scrap(manga,chapitre)
        compresse(manga,chapitre)
        file=discord.File(f"cbz/{manga}/{chapitre}.cbz")
        await interaction.edit_original_response(content=f"voila le chapitre",attachments=[file])
        supprime()
