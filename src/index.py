import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="Esto es un bot de ayuda")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="lorem impsum dolor",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Servidor creado el ",
                    value=f"{ctx.guild.created_at}")
    embed.add_field(name="Servidor creado por ", value=f"{ctx.guild.owner}")
    embed.add_field(name="Región del servidor ", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor ", value=f"{ctx.guild.id}")
    embed.set_thumbnail(
        url="https://estaticos.efe.com/efecom/recursos2/imagen.aspx?-P-2fL4Jfo8HOMhj8eo-P-2bNCyYYbMnS19Ym1maQ4TncnkXVSTX-P-2bAoG0sxzXPZPAk5l-P-2fU5UZEm-P-2bahXxHpGzFaLXE6v5cQ-P-3d-P-3d")
    await ctx.send(embed=embed)

@bot.command()
async def yt(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    #print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Con tu vieja", url="http://https://www.twitch.tv/"))
    print('El Bot está listo')


bot.run(TOKEN)
