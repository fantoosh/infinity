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


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    """ Responds Hi with an embedded message"""
    embed = Embeds(title="My Amazing Embed", description="Embeds are super easy, barely an inconvenience.")
    embed.create()
    embed.add_field(name="A Normal Field", value="**A really nice field with some information**")

    await ctx.respond("Hey!", embed=embed.to_dict())


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


@bot.command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')


cog_list = ['greetings']
for cog in cog_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(TOKEN)
