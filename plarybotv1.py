import discord
import json
import os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random


bot = commands.Bot(command_prefix = "pl")
bot.remove_command('help')
os.chdir('C:\\\Users\\user\\\Desktop\\\python.coding')
def is_digit(msg):
    return msg.content.isdigit()


#'beta phase,running on {} servers'.format(len(bot.servers)),type=3)
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='please do plapology!',type=2))
    print('logged in as',bot.user.name,'with an id of',bot.user.id,'!')

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
     elif message.content.upper().startswith('BUDDIN'):
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
        if user.mention != user.bot:
         await bot.send_message(channel,'{} has leveled up to level {}'.format(user.mention,lvl_end))
         users[user.id]['level'] = lvl_end


#await bot.say('{} is currently ***level***  {}'.format(user,(data[user.id]['level'])))
@bot.command(pass_context=True) #embed = discord.Embed(title='Name User', description='{}'.format(user.name), color=0xeee657)
async def rank(ctx,user:discord.Member):
    with open('users.json', 'r') as f:
     try:
      data = json.load(f)
      embed = discord.Embed(title='Name User', description='{}'.format(user), color=0xeee657)
      embed.add_field(name='Level:',value='{}'.format((data[user.id]['level'])))
      embed.set_footer(text='Note that it is a global rank we will add ranking soon :)')
      await bot.say(embed=embed)
     except:
      await bot.say('{} is not ranked yet!'.format(user))

@bot.command(pass_context=True)
async def apology(ctx):
    await bot.say('Hello,my name is Plary#3400.As of the apology,a bot attack happened in 18 August 2018.As the owner of the bot,I am highly sorry for what happened during that time.We found out the reason behind this problem,which is hacking caused on github.I will try to improve this bot security and then make this bot a better bot than usual.As always,sorry for what happened.')

@bot.command(pass_context=True)  #say hi to the bot
async def greets(ctx):
      await bot.say("yo hi")
      print('bot has been sucessfully greeted someone!')

@bot.command(pass_context=True)  #information about the bot
async def info(ctx):
    embed = discord.Embed(title='about Bot!', description='a very simple bot created by Plary#3400!', color=0xeee657)

    embed.add_field(name='Author', value='Plary#3400')

    embed.add_field(name='Invite:', value='https://discordapp.com/api/oauth2/authorize?client_id=473041869170016266&permissions=16787456&scope=bot')

    embed.add_field(name='Servers joined:', value='{}'.format(len(bot.servers)))

    embed.add_field(name='Help server:', value='https://discord.gg/NCvabEC')

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

    embed.add_field(name='greets',value='say hi to the bot!', inline=False)

    embed.add_field(name='info ',value='tells you about the bot!', inline=False)

    embed.add_field(name='about [user]',value='tells you information about a user', inline=False)

    embed.add_field(name='ping',value='returns ping', inline=False)

    embed.add_field(name='say [any words]',value='bot says what the user types', inline=False)

    embed.add_field(name='rank [user]', value='tells you about your current rank!', inline=False)

    embed.add_field(name='isay [any words]',value='funny meme', inline=False)

    embed.add_field(name='serverinfo',value='information about the server',inline=False)

    embed.add_field(name='shoutouts', value='list of cool people who helped for this develepment', inline=False)

    embed.add_field(name='spam [message] [number less than 11]',value='spams whatever you want!')

    embed.set_footer(text='having problems? dm plary#3400 or join the help server!Server link = https://discord.gg/NCvabEC')

    await bot.send_message(author,embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="{}".format(ctx.message.server.name))
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name='owner:',value=ctx.message.server.owner)
    embed.add_field(name='Region:',value=ctx.message.server.region)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def shoutouts(ctx):
    embed = discord.Embed(title='Thanks to:', description='list of people who helped throught the build of this bot', color=0xeee657)
    embed.add_field(name='BlueWateryLemon#8396',value='Best friend who likes to use Plaryboat',inline=False)
    embed.add_field(name='TZY#9517',value='Always test new commands with the owner!',inline=False)
    embed.add_field(name='Chronicle-Anarchy#6452',value='Likes to roast but then hes supporting',inline=False)
    embed.add_field(name='God Sans#0792',value='Likes to support alot which is cool',inline=False)
    embed.add_field(name='BUDDIN#6575',value='Likes to use my commands too',inline=False)
    embed.add_field(name='IcyxXxRexyxXx#9521',value='likes to support on moderating and commands',inline=False)
    embed.add_field(name='BEEP#1844',value='he likes to do commands and supports on this',inline=False)
    embed.set_footer(text='I love you guys all no homo uwu')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def spam(ctx,times:int,*,content:str):
    if times != None:
     if times <= 10:
         for spams in range(times):
             await bot.say(content)
     else:
          await bot.say('haha no')
    else:
        await bot.say('forgot one argument')


@bot.command(pass_context=True)
async def bombping(ctx,user:discord.Member):
    await bot.say((user.mention)*15)


@bot.command(pass_context=True)
async def delete(ctx):
    await bot.delete_message(ctx)
    await bot.say('deleted!')

@bot.command(pass_context=True)
async def getserverid(ctx):
    await bot.say('{}'.format(ctx.message.server.id))

@bot.command(pass_context=True)
async def premiumserver(ctx):
    servers = ['152977006978531329','399460952359305219','475209454447755275']
    if ctx.message.server.id in servers:
        await bot.send_message(ctx.message.channel,'This server is premium!')
    else:
        await bot.send_message(ctx.message.channel,'This server is not premium!')

@bot.command(pass_context=True)
async def guess(ctx):
    correct = random.randint(1,10)
    print(correct)
    await bot.say('put a number between 1 and 10')
    for chance in range(1,6):
     msg = await bot.wait_for_message(check=is_digit)
     answer = int(msg.content)
     if answer > correct:
          await bot.say('the anwser is smaller than the correct one.You only have {} use(s) left!'.format(5 - chance))
     elif answer < correct:
          await bot.say('the anwser is larger than the correct one.You only have {} use(s) left!'.format(5 - chance))
     elif answer == correct:
         await bot.say('congrats,you got the right number!')
         return None
     else:
         await bot.say('sorry,the anwser was {}'.format(correct))
         return None





bot.run('TOKEN')
