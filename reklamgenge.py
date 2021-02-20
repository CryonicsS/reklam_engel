import discord
import random
import asyncio
from discord.ext import commands
from discord import User
from discord.ext.commands import Bot, guild_only


intents=intents=discord.Intents.all()
intents = discord.Intents()
intents.members = True

client = commands.Bot(command_prefix = '*')

client.remove_command('help')

TOKEN = "TOKEN"

print("developed by cryonics")

link_filter = [".com", "http", "https:", ".gg", "discord."]



@client.listen('on_message')
async def message(message, member: discord.Member = None):

    if message.author.id == # BOT VEYA ADMİN İDLERİ ORAAYI YAPARSANIZ YAPAMAZSANIZ YAZIN DC : cryonics#4301
        return

        
    for word in link_filter:
        if message.content.count(word) > 0:
            await message.channel.purge(limit=1)

            embed = discord.Embed(
                    
            colour = discord.Colour.red())
                
            embed.set_footer(text=f"Lütfen reklam yapma")
            embed.add_field(name=f"Reklam yasak", value=(message.author.mention) + ', Şimdilik mesajını sildim bir daha olursa .....', inline=False)
            await message.channel.send(embed=embed, delete_after=15)



client.run(TOKEN)
