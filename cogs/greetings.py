import discord
from discord.ext import commands


class Greetings(discord.Cog):  # Create a class that inherits from commands.Cog
    # This clas is used to create a Cog, which is a module that we can add to our bot
    def __init__(self, bot):  # This is a special method that is called when the cog is loaded
        self.bot = bot

    #  All methods must have self and ctx parameters

    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hi to {member.mention}!')

    @discord.slash_command()  # An Application command
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Welcome to the server!')


def setup(bot):  # This is called by py-cord to set up the bot
    bot.add_cog(Greetings(bot))
