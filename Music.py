import discord
from discord.ext import commands


# """music commands for Plaryboat
#   credits to Lucas Kumara for all heads up"""

class Music:
    def __init__(self,bot): #self and the bot variable
        self.bot = bot

    async def on_message_delete(self,message):
        print('message deleted')


    @commands.command()
    async def oof(self):
        await self.bot.say('pong')







def setup(bot):
    bot.add_cog(Music(bot))
