import discord
from discord.ext import commands


class moderation:
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,user:discord.Member,*,reason:str):
        await self.bot.kick(user)
        await self.bot.say('successfully kicked {} for **{}**'.format(user,reason))
        await self.bot.send_message(user,'you got kicked for **{}**'.format(reason))


    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,user:discord.Member,*,reason:str):
        await self.bot.ban(user)
        await self.bot.say('{} has been banned due to ***{}***'.format(user,reason))
        await self.bot.send_message(user,'you got banned for ***{}***'.format(reason))

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,user:discord.Member):
        await self.bot.unban(user)
        await bot.say('unbanned {}'.format(user))





def setup(bot):
    bot.add_cog(moderation(bot))
