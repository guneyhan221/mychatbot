import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def factoriel(ctx,x):
    x=int(x)
    if x in [0,1]:
        await ctx.send("1'den büyük bir sayı giriniz!")
        return   
    num=1
    for i in range(2,x+1):
        num*=i  
    await ctx.send(f"{x}!={num}")



bot.run("TOKEN HERE!")
