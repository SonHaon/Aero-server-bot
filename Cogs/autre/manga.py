import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
from requests import get
from scrapy import Selector
import os
import shutil
import os
from PIL import Image

def manga_exist(manga):
    if get(f"https://lelscanvf.cc/manga/{manga}").status_code != 200:
        return False
    else:
        return True
    
def chap_exist(manga,chap):
    if get(f"https://lelscanvf.cc/manga/{manga}/{chap}").status_code != 200:
        return False
    else:
        return True

def file_create(manga,chap):
    if not os.path.exists("img"):
        os.mkdir("img")
    if not os.path.exists(f"img/{manga}"):
        os.mkdir(f"img/{manga}")
    if not os.path.exists(f"img/{manga}/{chap}"):
        os.mkdir(f"img/{manga}/{chap}")
    if not os.path.exists("cbz"):
        os.mkdir(f"cbz")
    if not os.path.exists(f"cbz/{manga}"):
        os.mkdir(f"cbz/{manga}")

def scrap(manga,chap):
    for i in range(100):
        reponse = get(url=f"https://lelscanvf.cc/manga/{manga}/{chap}/{i+1}")
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
                with open(f"img/{manga}/{chap}/{i+1}.jpg","wb") as f:
                    f.write(test.content)
        if len(images) ==1:
            return i      

def compresse(manga,chap,nb_image):
    for i in range(nb_image):
        im1 = Image.open(f"img/{manga}/{chap}/{i+1}.jpg")
        im1 = im1.convert("RGB")
        im1.save(f"img/{manga}/{chap}/{i+1}.jpg",format="JPEG",optimize=True,quality=10)
        im1.close()

def create_cbz(manga,chap):
    shutil.make_archive(f"img/{manga}/{chap}","zip",f"img/{manga}/{chap}")
    if os.path.exists(f"cbz/{manga}/{chap}.cbz"):
        os.remove(f"cbz/{manga}/{chap}.cbz")
    os.rename(f"img/{manga}/{chap}.zip",f"cbz/{manga}/{chap}.cbz")

def supprime(nb_image,manga,chap):
    for i in range(nb_image):
        os.remove(f"img/{manga}/{chap}/{i+1}.jpg")


class manga(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    
    @app_commands.command(name="manga_scan",description="envoie un fichier du chapitre du manga voulu")
#    @app_commands.choices(manga= [
#        app_commands.Choice(name=f"One Piece",value="one-piece"),
#        app_commands.Choice(name="Naruto",value="naruto"),
#        app_commands.Choice(name="Dragon ball Super",value="dragon-ball-super"),
#        app_commands.Choice(name="My Hero Academia",value="my-hero-academia")
#    ])
    @app_commands.rename(chap="chapitre")
    async def manga(self,interaction:discord.Interaction,manga:str,chap:str):
        manga="-".join(manga.split(" "))
        await interaction.response.defer(ephemeral=True)
        if not os.path.exists(f"cbz/{manga}/{chap}.cbz"):
            if not manga_exist(manga):
                print("ce manga est introuvable")
            elif not chap_exist(manga,chap):
                print("ce chapitre est indisponible")
            else:
                file_create(manga,chap)
                nb_image=scrap(manga,chap)
                compresse(manga,chap,nb_image)
                create_cbz(manga,chap)
                file=discord.File(f"cbz/{manga}/{chap}.cbz")
                supprime(nb_image,manga,chap)
                await interaction.edit_original_response(content=f"je te l'ai télécharger, le voila",attachments=[file])
        else:
            file=discord.File(f"cbz/{manga}/{chap}.cbz")
            await interaction.edit_original_response(content=f"je l'avait déjà, le voila",attachments=[file])
        
