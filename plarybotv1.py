#source:https://github.com/Plaryda/plarybot
#read License.txt before checking

import discord
import json
import os
from discord.ext import commands
import asyncio
import random
import time
from time import sleep
import pathlib
import datetime


bot = commands.Bot(command_prefix = "pl")
bot.remove_command('help')
user_path = pathlib.Path(__file__).parent.joinpath('users.json')
def is_digit(msg):
    return msg.content.isdigit()

start_time = time.time()
fullda = time.strftime("%a, %d %b %Y %H:%M ", time.gmtime())

extensions = ['CommandErrorHandler','Music','moderation']



#'beta phase,running on {} servers'.format(len(bot.servers)),type=3)
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='{} servers  || bot is 24/7!'.format(len(bot.servers)),type=3))
    print('logged in as',bot.user.name,'with an id of',bot.user.id,'!')

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension,error))




@bot.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users,member)

    with open('users.json', 'w') as f:
        json.dump(users,f)


@bot.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)
    await bot.process_commands(message)
    if message.author != message.author.bot:
     print('[{}]{}'.format(message.author,message.content))
     if message.content.upper().startswith('OOFS'):
       await bot.send_message(message.channel,'oof!')
     elif message.content.upper().startswith('UNDERSTANDABLE'):
       await bot.send_message(message.channel,'have a nice day')
     elif message.content.upper().startswith('AMIOWNER'):
         if message.author.id == '152976541373038592':
             await bot.send_message(message.channel,'you are my daddy,nya~')
         else:
             await bot.send_message(message.channel,'you are not my daddy :cri:')
     if message.content.upper().startswith('VORTEX'):
        await bot.send_message(message.channel,'is gay')
     elif message.content.upper().startswith('WHOISAFAG'):
         await bot.send_message(message.channel,'plary is :D')
     elif message.content.upper().startswith('BALDI'):
         await bot.send_message(message.channel,'https://media.discordapp.net/attachments/257695856986292224/481554460741730324/b.gif https://media.discordapp.net/attachments/257695856986292224/481554509814956037/al.gif https://media.discordapp.net/attachments/257695856986292224/481554525342269440/di.gif')

    await update_data(users, message.author)
    await add_experience(users,message.author,5)
    await level_up(users,message.author,message.channel)

    with open('users.json', 'w') as f:
        json.dump(users,f)

async def update_data(users,user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users,user,experience):
    users[user.id]['experience'] += experience


async def level_up(users,user,channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
         await bot.send_message(channel,'{} has leveled up to level {}'.format(user.mention,lvl_end))
         users[user.id]['level'] = lvl_end


#await bot.say('{} is currently ***level***  {}'.format(user,(data[user.id]['level'])))
@bot.command(pass_context=True) #embed = discord.Embed(title='Name User', description='{}'.format(user.name), color=0xeee657)
async def rank(ctx,user:discord.Member):
    with open('users.json', 'r') as f:
     try:
      vip = ['152976541373038592','409137017755140097','472382614347448360','177840117057191937','392986213113528322','424972995535306763']
      data = json.load(f)
      embed = discord.Embed(title='Name User', description='{}'.format(user), color=0xeee657)
      embed.add_field(name='Level:',value='{}'.format((data[user.id]['level'])))
      embed.add_field(name='Premium:',value='{}'.format(user.id in vip))
      embed.set_footer(text='Note that it is a global rank we will add ranking soon :)')
      embed.set_thumbnail(url=user.avatar_url)
      await bot.say(embed=embed)
     except:
      await bot.say('{} is not ranked yet!'.format(user))

@bot.command()
async def load(extension):
    if ctx.message.author.id == '152976541373038592':
        try:
            bot.load_extension(extension)
            print('loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension,error))
    else:
        raise NotHavePermission

@bot.command()
async def unload(extension):
    if ctx.message.author.id == '152976541373038592':
        try:
            bot.unload_extension(extension)
            print('unloaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be unloaded [{}]'.format(extension,error))
    else:
        raise NotHavePermission

@bot.command(pass_context=True)
async def coinflip(ctx):
    anwser = ['heads!','tails!']
    await bot.say(random.choice(anwser))

@bot.command(pass_context=True)  #information about the bot
async def info(ctx):
    embed = discord.Embed(title='about Bot!', description='a very simple bot created by Plary#3400!', color=0xeee657)

    embed.add_field(name='Author', value='Plary#3400')

    embed.add_field(name='Invite:', value='https://discordapp.com/api/oauth2/authorize?client_id=473041869170016266&permissions=16787456&scope=bot')

    embed.add_field(name='Servers joined:', value='{}'.format(len(bot.servers)))


    embed.add_field(name='Help server:', value='https://discord.gg/NCvabEC')

    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/152976541373038592/5dcd9767b0b98b8b15411420d00d1270.png?size=1024')

    embed.set_footer(text='having problems?come contact Plary#3400 in DMs!')


    await bot.say(embed=embed)
    print("someone checked the info!")

@bot.command(pass_context=True) #about user who got pinged
async def about(ctx, user: discord.Member):

    embed = discord.Embed(title='Name User', description='{}'.format(user.name), color=0xeee657)

    embed.add_field(name='ID', value='{}'.format(user.id))

    embed.add_field(name='Top role', value='{}'.format(user.top_role))

    embed.add_field(name='Top permission', value='{}'.format(iter(user.server_permissions)))

    embed.add_field(name='Discrim:',value='#{}'.format(user.discriminator))

    embed.add_field(name='Time Created:',value='{}'.format(user.created_at))


    embed.set_thumbnail(url=user.avatar_url)

    await bot.say(embed=embed)

    print('someone has checked the information about an user!')

@bot.command(pass_context=True) #returns ping
async def ping(ctx):
      await bot.say('angery pong reeee!')
      print('someone just got pinged!')

@bot.command(pass_context=True) #returns the output as the user sends
async def say(ctx,*,content:str):
    await bot.delete_message(ctx.message)
    await bot.say(content)


@bot.command(pass_context=True)
async def changelog(ctx):
    text = '``19/9`` - bot is officially 24/7!\n``20/9`` - this command is created;fixed plguess and disabled plspam for time being\n``22/9`` - bot added moderation commands'
    await bot.say(text)


@bot.command(pass_context=True)
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    await bot.say('Uptime: ``{}``\nStart Time: ``{}``'.format(text,fullda))
    print('debug')




@bot.command(pass_context=True) #funny meme,maybe
async def isay(ctx, user:discord.Member,*,content:str):
    await bot.say('{} says "{}"'.format(user.name,content))


@bot.command(pass_context=True) #help
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color = discord.Colour.orange()
    )
    embed.set_author(name='help')

    embed.add_field(name='Fun',value='``plspam [limit<=10] [message]`` - spams,duh!\n``isay [user] [content]`` - great troll!\n``mythtime`` - will ping you at random time!\n``rps [rock,paper,scissors]`` - plays the rock paper scissors game\n``guess`` - a simple guess game\n``say`` - make the bot to say what you want!\n``bombping [user]`` - pings a user 15 times in one line\n ``coinflip`` - head or tails?')

    embed.add_field(name='Utility',value='``checkmessages`` - gives how much messages has been sent!\n``getseverid``- gives id of a server!\n``changelog`` - shows update of this bot!\n``serverinfo`` - information about the server\n``info`` - information about the bot\n``shoutouts`` - list of cool people who helped in this bot\n``rank [user]`` - shows a rank of a user\n``premium`` - shows a premium server\n``ping`` pings you\n``vipcheck [user]`` - to check vip status\n``about [user]`` - sends info about a user\n``uptime`` - gives uptime of the bot')

    embed.add_field(name='Moderation',value='``kick`` - kicks a user \n``ban`` - bans a user')

    embed.set_footer(text='having problems? dm plary#3400 or join the help server!Server link = https://discord.gg/NCvabEC')

    await bot.send_message(author,embed=embed)
    await bot.say(':white_check_mark: help has been sent to you!')


@bot.command(pass_context=True)
async def serverinfo(ctx):
    servers = ['152977006978531329','399460952359305219','475209454447755275','424972995535306763']
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="{}".format(ctx.message.server.name))
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name='owner:',value=ctx.message.server.owner)
    embed.add_field(name='Region:',value=ctx.message.server.region)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name='Premium',value='{}'.format(ctx.message.server.id in servers))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def shoutouts(ctx):
    embed = discord.Embed(title='Thanks to:', description='list of people who helped throught the build of this bot', color=0xeee657)
    embed.add_field(name='BlueWateryLemon#8396',value='Best friend who likes to use Plaryboat',inline=False)
    embed.add_field(name='TZY13#9517',value='Always test new commands with the owner!',inline=False)
    embed.add_field(name='Chronicle-Anarchy#6452',value='Likes to roast but then hes supporting',inline=False)
    embed.add_field(name='God Sans#0792',value='Likes to support alot which is cool',inline=False)
    embed.add_field(name='BUDDIN#6575',value='Likes to use my commands too',inline=False)
    embed.add_field(name='IcyxXxRexyxXx#9521',value='likes to support on moderating and commands',inline=False)
    embed.add_field(name='BEEP#1844',value='he likes to do commands and supports on this',inline=False)
    embed.add_field(name='Adib Rafique',value='he is cool and helps to test only games',inline=False)
    embed.set_footer(text='I love you guys all no homo uwu')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def spam(ctx,times:int,*,content:str):
    if ctx.message.author.id != 152976541373038592:
        await bot.say('this command is temporaily disabled!')
    else:
        if times != None:
            if times <= 10:
                for spams in range(times):
                    await bot.say(content)
            else:
                await bot.say('max is 10,says god sans')
        else:
            await bot.say('forgot one argument')

@bot.command(pass_context=True)
async def rps(ctx,anwser:str):
    anwsers = ['rock','paper','scissors']
    anwsers2 = anwsers[random.randint(0,2)]
    print(anwsers2)
    #rock beats scissors
    #scissors beats paper
    #paper beats rock
    #if [x] fights with non default than[y],[x] will lose.
    if anwser == anwsers2:
        await bot.say('its a tie!, i chose {} and so is you!'.format(anwsers2))
    elif anwser == 'rock':
        if anwsers2 == 'scissors':
            await bot.say('hah!,you won!') #[x] beats [y]
        else:
            await bot.say('ayy lmao you lost,i chose {}'.format(anwsers2)) #non default
    elif anwser == 'paper':
        if anwsers2 == 'rock':
            await bot.say('hah!,you won!')
        else:
            await bot.say('ayy lmao you lost,i chose {}.'.format(anwsers2))
    else:
        if anwser == 'scissors':
            if anwsers2 == 'paper':
                await bot.say('hah!,you won!')
            else:
                await bot.say('ayy lmao you lost,i chose {}.'.format(anwsers2))

@bot.command(pass_context=True) #makes to ping user when reached [myth2]s
async def mythtime(ctx):
    while True:
        await bot.say('the time starts now,what could it be?')
        myth2 = random.randint(1,(10))
        for myth in range(myth2):
            sleep(1)
            if myth == myth2 - 1:
                await bot.say('{}, your random timer ended at ``{}s``!'.format(ctx.message.author.mention,myth2))
                return False





@bot.command(pass_context=True)
async def bombping(ctx,user:discord.Member):
    await bot.say((user.mention)*15)




@bot.command(pass_context=True)
async def getserverid(ctx):
    await bot.say('{}'.format(ctx.message.server.id))

@bot.command(pass_context=True)
async def premium(ctx):
    servers = ['152977006978531329','399460952359305219','475209454447755275','424972995535306763']
    if ctx.message.server.id in servers:
        await bot.send_message(ctx.message.channel,'This server is premium!')
    else:
        await bot.send_message(ctx.message.channel,'This server is not premium!')

@bot.command(pass_context=True)
async def guess(ctx):
    if ctx.message.author.id != '152976541373038592':
        await bot.say('the command is temporaily disabled!')
    else:
        correct = random.randint(1,10)
        print(correct)
        await bot.say('put a number between 1 and 10')
        while True:
            for chance in range(1,6):
                    msg = await bot.wait_for_message(check=is_digit)
                    answer = int(msg.content)
                    if answer > correct:
                        await bot.say('the anwser is smaller than the correct one.You only have {} use(s) left!'.format(5 - chance))
                    elif answer < correct:
                        await bot.say('the anwser is larger than the correct one.You only have {} use(s) left!'.format(5 - chance))
                    else:
                        return False
            if answer == correct:
                await bot.say('congrats,you got the right number!')
                return False
            else:
                await bot.say('sorry,the anwser was {}'.format(correct))
                return False


@bot.command(pass_context=True)
async def timer(ctx,time:int):
    userID = ctx.message.author.id
    await bot.say('starting the timer from ``{}s`` now!'.format(time))
    while True:
        for woahs in range(time + 2):
            sleep(1)
            if woahs == time - 1:
                await bot.say('Hey <@{}>,time is up! you started from ``{}s``!'.format(userID,time))
                return False

@bot.command(pass_context=True)
async def vipcheck(ctx,user:discord.Member):
    vip = ['152976541373038592','409137017755140097','472382614347448360','177840117057191937','392986213113528322']
    if user.id in vip:
        await bot.say('he/she are vip,cool!')
    else:
        await bot.say('he/she are not vip cri')
    if ctx.message.author.id == user.id  in vip:
        await bot.say('you are vip,cool!')
    else:
        await bot.say('you are not vip,cri')

@bot.command(pass_context=True)
async def checkmessages(ctx):
    while ctx.message.author.id == '152976541373038592':
        await bot.say('the bot is currently sending {} messages'.format(len(bot.messages)))
        return False


@bot.command(pass_context=True)
@commands.cooldown(1,30,commands.BucketType.channel)
async def testcooldown(ctx):
         await bot.say('yeet')

@testcooldown.error
async def testcooldown_handler(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        print('command used!')
        if error.param.name == 'ctx':
            await bot.send("the command is in cooldown")

#https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612


#
#  """Below is an example of a Local Error Handler for our command do_repeat"""
# @commands.command(name='repeat', aliases=['mimic', 'copy'])
# async def do_repeat(self, ctx, *, inp: str):
#         """A simple command which repeats your input!
#         inp  : The input to be repeated"""
#
#     await ctx.send(inp)
#
# @do_repeat.error
# async def do_repeat_handler(self, ctx, error):
#         """A local Error Handler for our command do_repeat.
#         This will only listen for errors in do_repeat.
#         The global on_command_error will still be invoked after."""
#
#         # Check if our required argument inp is missing.
#     if isinstance(error, commands.MissingRequiredArgument):
#         if error.param.name == 'inp':
#             await ctx.send("You forgot to give me input to repeat!")

bot.run(os.getenv('TOKEN'))
