import discord
from discord.ext import commands


class Games(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Play Guess the number game")
    async def gtn(self, ctx):
        await ctx.respond('Guess a number between 1 and 10')
        guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

        if int(guess.content) == 5:
            await ctx.send('You Guessed It!')
        else:
            await ctx.send('Nope! Try again.')


def setup(bot):
    bot.add_cog(Games(bot))
