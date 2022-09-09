import discord
import logging

from settings import TOKEN
from utils.config import Embeds

# Set up logging handler
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# setting intents
intents = discord.Intents.all()

bot = discord.Bot(debug_guilds=[951434878799446026], intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="introduction", description="Get name and Age from member")
async def get_details(
    ctx: discord.ApplicationContext,
    name: discord.Option(str, "Enter your name"),
    age: discord.Option(int, "Enter your age", min_value=1, max_value=99, default=18)
    # passing the default value makes an argument optional
    # you also can create optional argument using:
    # age: Option(int, "Enter your age") = 18
):
    await ctx.respond(f"Hello! Your name is {name} and you are {age} years old.")


# Loading cogs
cog_list = ['greetings', 'games']
for cog in cog_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(TOKEN)
