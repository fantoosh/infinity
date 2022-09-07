import discord
import logging

from settings import TOKEN
from utils.config import Embeds

# Set up logging handler
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
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
    """
    embed = discord.Embed(
        title="My Default Embed",
        description="Making my first Embed.",
        color=discord.Colour.dark_gold(), # pycord provides a class with default colours
    )
    embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown**")

    embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
    embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
    embed.add_field(name="Inline Field 3", value="Inline Field 3", inline=True)

    embed.set_footer(text="Footer! No markdown here.")  # footers can have icons too
    embed.set_author(name="Pycord Team", icon_url="https://example.com/link-to-my-image.png")
    embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
    embed.set_image(url="https://example.com/link-to-my-banner.png")

    await ctx.respond("Hey!", embed=embed)
    """
    embed = Embeds(title="My Amazing Embed", description="Embeds are super easy, barely an inconvenience.")
    embed.create()
    embed.add_field(name="A Normal Field", value="**A really nice field with some information**")

    await ctx.respond("Hey!", embed=embed.to_dict())


@bot.command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')


bot.run(TOKEN)
