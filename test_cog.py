import discord
from discord.ext import commands

class testcog:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def joined(self, member : discord.Member):
        """Says when a member joined."""
        await self.bot.say('{0.name} joined in {0.joined_at}'.format(member))

def setup(bot):
    bot.add_cog(testcog(bot))
