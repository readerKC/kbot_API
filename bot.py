import discord
import requests

from discord.ext import commands

 intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event

async def on_ready():

    print(f'{bot.user} olarak giriş yaptık')


def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

 bot.run("")
