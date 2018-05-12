import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import urbandict

Client = discord.Client()
client = commands.Bot(command_prefix = "-")
client.remove_command('help')



@client.event
async def on_ready():
    print("Bot is ready!")
    
	
@client.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.CommandOnCooldown):
		await client.send_message(ctx.message.channel, content='Calm down! You have to wait %.2f seconds before using new command :clock1:' % error.retry_after)
	raise error 		
	
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='-help'))
	

@client.command(pass_context=True)
async def idk2(ctx):
	embed = discord.Embed(title="Welcome to Infernal!", description="Infernal is launched in May of 2018 and was founded by Trocir. Infernal is led by Trocir. The clan does not use any extensions or mods and the players are popular for their legit and fair playstyle.", color=0xFF8C00)
	await client.say(embed=embed)	
	

@client.command(pass_context=True)
async def exdee(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="Rules", value="1 - Post in the appropriate channels. \n2 - Excessive name calling, harassment, or threats will not be tolerated and will result in a punishment. \n3 - Staff and Moderators decisions are final. Please respect them and the processes they use. \n4 - No discussion about highly illegal activity. \n5 - Do not post any NSFW, malware, or any other content that may be deemed offensive. \n6 - Be respectful of each other and keep discussions constructive. \n7 - Do not spam. \n8 - No (random) links in the general chat #general unless a moderator or higher lets you!")
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def idk(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="Roles", value="<@&442436870656360469> - The Leader of the team \n <@&442436324402659328> - Official Members \n <@&442648846338752513> - Official Bot \n <@&442442489404850176> - Important People \n <@&442443800447549442> - Special People \n <@&442440578710372352> - Special Guests \n <@&442440784709550083> - The girls \n <@&437282617885458432> - Default role \n <@&436460911192965121> - Server bots")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True, description='Shows the server info.')
async def server(ctx):
	embed = discord.Embed(description="Here's what I could find:", color=0x00ff00)
	embed.add_field(name="Name", value=ctx.message.server.name)
	embed.add_field(name="Owner", value=ctx.message.server.owner)
	embed.add_field(name="Region", value=ctx.message.server.region)
	embed.add_field(name="Roles", value=len(ctx.message.server.roles))
	embed.add_field(name="Members", value=len(ctx.message.server.members))
	embed.add_field(name="Channels", value=len(ctx.message.server.channels))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await client.say(embed=embed)
	
	
@client.command(pass_context=True, description='Shows the info of the mentioned user.')
async def info(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find:", color=0x00ff00)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=True)
	embed.add_field(name="Highest role", value=user.top_role)
	embed.add_field(name="Joined",value=user.joined_at)
	embed.set_thumbnail(url = user.avatar_url)
	await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(title="__About Feed Me__", description="© 2018 Feed Me Bot All Rights Reserved", color=0x00ff00)
	embed.add_field(name="Original Creators", value="<@399567243744116738> & <@293447483818901504>")
	embed.add_field(name="Co-Creator", value="<@331876823443177473>")
	embed.add_field(name="Server count", value=str(len(client.servers)))
	embed.add_field(name="User count", value=str(len(list(client.get_all_members()))))
	embed.add_field(name="Channel count",value=str(len(list(client.get_all_channels()))))
	embed.add_field(name="API", value="Python")
	embed.set_thumbnail(url='https://media.discordapp.net/attachments/438003912184692738/438306520317427712/Test.png?width=334&height=341')
	await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def trocir(ctx):
    embed = discord.Embed(title="__Trocir's profile__ :flag_rs:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)
	

@client.command(pass_context=True)
async def microhype(ctx):
    embed = discord.Embed(title="__MicroHype's profile__ :flag_gb:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def sm4ck(ctx):
    embed = discord.Embed(title="__Sm4ck's profile__ :flag_ps:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)
	

@client.command(pass_context=True)
async def avenger434(ctx):
    embed = discord.Embed(title="__Avenger434's profile__ :flag_my:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def mhmmyeeesss(ctx):
    embed = discord.Embed(title="__MhmmYeeesss's profile__ :flag_us:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def acquah(ctx):
    embed = discord.Embed(title="__Acquah's profile__ :flag_it:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def reddragon6(ctx):
    embed = discord.Embed(title="__RedDragon6's profile__ :flag_pk:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def alex2810(ctx):
    embed = discord.Embed(title="__Alex2810's profile__ :flag_ca:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def nahojaa(ctx):
    embed = discord.Embed(title="__Naho jaa's profile__ :flag_br:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="9th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def numbskullian(ctx):
    embed = discord.Embed(title="__Numb Skullian's profile__ :flag_gb:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="9th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)	
	

@client.command(pass_context=True)
async def nasean79(ctx):
    embed = discord.Embed(title="__nasean79's profile__ :flag_us:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="10th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)		
	
	
	
@client.command(pass_context=True)
async def records(ctx):
    embed = discord.Embed(title="__Feed Me Records__", description="Our Football Records", color=0x2874A6)
    embed.add_field(name="Biggest Win", value="Team 0-0 Team")
    embed.add_field(name="Most Goals in a match", value="Player - 0", inline = False)
    embed.add_field(name="Most Assists in a match", value="Player - 0", inline = False)
    embed.add_field(name="Most Goals of all time", value="Player - 0", inline = False)
    embed.add_field(name="Most Assists of all time", value="Player - 0", inline = False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
    await client.say(embed=embed)
	
	
	
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s avatar".format(user.name), color=0x00BFFF)
	embed.set_image(url = user.avatar_url)
	await client.say(embed=embed)	
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def multi(ctx, a,b):
	c=int(a) * int(b)
	s=str(c)
	await client.say(a + " * " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def sub(ctx, a,b):
	c=int(a) - int(b)
	s=str(c)
	await client.say(a + " - " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def add(ctx, a,b):
	c=int(a) + int(b)
	s=str(c)
	await client.say(a + " + " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def div(ctx, a,b):
	c=int(a) / int(b)
	s=str(c)
	await client.say(a + " / " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
async def choose(ctx,message):
	x=message.split("/")
	await client.say(":thinking:  |  I choose: "+ "**"+ random.choice(x) +"**!")



@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await client.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description=':ping_pong: Pong! `{}ms`'.format(round((t2-t1)*1000)), color=0x2874A6)
	await client.say(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def meme(ctx):
	list=['http://i0.kym-cdn.com/photos/images/facebook/001/217/729/f9a.jpg','http://mojly.com/wp-content/uploads/2017/10/Hilarious-Meme-humor-pictures-images-fun-thug-life-funny-meme.jpg','http://cdn.ebaumsworld.com/mediaFiles/picture/2407036/84822802.jpg','http://images.memes.com/meme/29838.jpg','http://images.memes.com/meme/9076.jpg','http://images.memes.com/meme/14834.jpg','http://images.memes.com/meme/10828.jpg','http://images.memes.com/meme/25719.jpg','http://images.memes.com/meme/20837.jpg','http://images.memes.com/meme/27526.jpg','https://i.redd.it/3n3lixsq5vq01.jpg','https://i.redd.it/xovz0z5mewq01.jpg','https://i.redd.it/kqsotjgj0yq01.jpg','http://images.memes.com/meme/868122','http://images.memes.com/meme/1452777','http://images.memes.com/meme/19242.jpg','http://images.memes.com/meme/1111179','https://i.redd.it/cva9tb3r1wq01.png','https://imgur.com/2hlsj7Q','https://i.redd.it/f5l79kk17yq01.jpg','https://i.redd.it/ii9w5dpqyxq01.jpg','https://imgur.com/UH6DABG','https://i.redd.it/5zo511n7bxq01.jpg','https://i.redd.it/dxefclltiyq01.jpg']
	secure_random = random.SystemRandom()
	m=secure_random.choice(list)
	embed = discord.Embed(description="Random Meme", color=0x00BFFF)
	embed.set_image(url=m)
	await client.say(embed=embed)

	
@client.command()
async def urban(*, word: str):
	try:
		defi = urbandict.define(word)
		definition = defi[0]['def']
		example = defi[0]['example']
		embed = discord.Embed(title=word, description=definition, color=0x0062f4)
		embed.add_field(name="Example", value=example, inline=False)
		embed.set_footer(text="Urban Dictionary")
		await client.say(embed=embed)
	except:
		await client.say(":exclamation: Error. No definition found.")
			


client.run("NDQzMDczNzMyMTg2MDc5MjM1.DdIETg._dnErZuMYPs9zWGVhMVOPOF7i6Q")
