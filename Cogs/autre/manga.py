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
import typing

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
    for i in range(1000):
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
                if name.startswith(" https"):
                    name = f"h{name.removeprefix(' h').removesuffix('g ')}g"
                else:
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

manga_list = ["One Piece","Naruto","Dragon ball Super","My Hero Academia","Black Clover","Jujutsu Kaisen","One Punch Man","Eden's Zero","Mashle","Solo Leveling","Boruto"]

class manga(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    async def manga_autocompletion(
        self,
        interaction:discord.Interaction,
        current:str
    ) -> typing.List[app_commands.Choice[str]]:
        data=[]
        for manga in manga_list:
            if current.lower() in manga.lower():
                data.append(app_commands.Choice(name=manga,value=manga.replace("'","")))
        return data


    @app_commands.command(name="manga_scan",description="envoie un fichier du chapitre du manga voulu")
#    @app_commands.choices(manga= [
#        app_commands.Choice(name=f"One Piece",value="one-piece"),
#        app_commands.Choice(name="Naruto",value="naruto"),
#        app_commands.Choice(name="Dragon ball Super",value="dragon-ball-super"),
#        app_commands.Choice(name="My Hero Academia",value="my-hero-academia")
#    ])
    @app_commands.autocomplete(manga=manga_autocompletion)
    @app_commands.rename(chap="chapitre")
    async def manga(self,interaction:discord.Interaction,manga:str,chap:str):
        manga="-".join(manga.split(" ")).lower()
        await interaction.response.defer(ephemeral=True)
        if not os.path.exists(f"cbz/{manga}/{chap}.cbz"):
            if not manga_exist(manga):
                await interaction.edit_original_response(content=f"Désolé, je ne trouve pas ce manga. \nsoit tu t'es trompé dans le nom soit il n'est pas disponible sur le site où je télécharge mes mangas")
            elif not chap_exist(manga,chap):
                await interaction.edit_original_response(content=f"Désolé, je ne trouve pas ce chapitre. \nsoit il n'est pas encore sorti soit il n'est pas encore disponible sur le site où je télécharge mes chapitres")
            else:
                await interaction.edit_original_response(content=f"<a:loading:1141362851206922300> Veuillez patienter le temps du téléchargement <a:loading:1141362851206922300>")
                file_create(manga,chap)
                nb_image=scrap(manga,chap)
                await interaction.edit_original_response(content=f"<a:loading:1141362851206922300> Je l'ai téléchargé, je te fais un beau petit fichier et je te l'envoie <a:loading:1141362851206922300>")
                compresse(manga,chap,nb_image)
                create_cbz(manga,chap)
                file=discord.File(f"cbz/{manga}/{chap}.cbz")
                supprime(nb_image,manga,chap)
                await interaction.edit_original_response(content=f"tiens le voila",attachments=[file])
        else:
            file=discord.File(f"cbz/{manga}/{chap}.cbz")
            await interaction.edit_original_response(content=f"je l'avait déjà, le voila",attachments=[file])
        
