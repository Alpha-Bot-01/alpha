import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

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

		

@client.command(pass_context=True, description='Shows the info of the mentioned user.')
async def info(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find:", color=0x00ff00)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=True)
	embed.add_field(name="Highest role", value=user.top_role)
	embed.add_field(name="Joined",value=user.joined_at)
	await client.say(embed=embed)
	
	
	
	
@client.command(pass_context=True, description='Shows the server info.')
async def server(ctx):
	embed = discord.Embed(name="{}'s info".format(ctx.message.server.name),description="**Server Stats:** ", color=0x00ff00)
	embed.add_field(name="Name", value=ctx.message.server.name)
	embed.add_field(name="Roles", value=len(ctx.message.server.roles))
	embed.add_field(name="Members", value=len(ctx.message.server.members))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await client.say(embed=embed)

	
	
@client.command(pass_context=True)
async def stats(ctx):
    embed = discord.Embed(description="Alpha Bot Stats:", color=0x00ff00)
    embed.add_field(name="Bot made by:", value="Trocir#1816 & Mes#1807")
    embed.add_field(name="Bot ID:", value="396458108987244563")
    embed.add_field(name="User count:", value=str(len(list(client.get_all_members()))))
    embed.add_field(name="Server count:", value=str(len(client.servers)))
    await client.say(embed=embed)		

	
	
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
		url=user.avatar_url
		await client.say(url)
	
	
	
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
async def help(ctx):
    embed = discord.Embed(description="", color=0x00BFFF)
    embed.add_field(name=" :scroll: Command list and Description: ", value="\n Prefix is - \n \n-ping = Pings the bot. \n-add = Adds the two entered numbers. (Example = -add 10 50) \n-sub = Subtracts the two entered numbers. (Example = -sub 10 50) \n-multi = Multiplies the two entered numbers. (Example = -multi 10 50) \n-div = Divides the two entered numbers. (Example = -div 10 50) \n-choose = Chooses one option from the list. (Example = -choose 1/2/3, do not put space between options.) \n-8ball = Answers your yes/no questions. \n-avatar = Displays the avatar of the mentioned user. (Example = -avatar <user>) \n-info = Displays the mentioned users info. (Example = -info <user>) \n-server = Displays the server stats. \n-stats = Shows the stats of the bot.")
    await client.say(embed=embed)
	
	
	
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
	embed=discord.Embed(title=None, description=':ping_pong: Pong! `{}miliseconds`'.format(round((t2-t1)*1000)), color=0x2874A6)
	await client.say(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def meme(ctx):
	list=['http://i0.kym-cdn.com/photos/images/facebook/001/217/729/f9a.jpg','http://mojly.com/wp-content/uploads/2017/10/Hilarious-Meme-humor-pictures-images-fun-thug-life-funny-meme.jpg','http://cdn.ebaumsworld.com/mediaFiles/picture/2407036/84822802.jpg','http://images.memes.com/meme/29838.jpg','http://images.memes.com/meme/9076.jpg','http://images.memes.com/meme/14834.jpg','http://images.memes.com/meme/10828.jpg','http://images.memes.com/meme/25719.jpg','http://images.memes.com/meme/20837.jpg','http://images.memes.com/meme/27526.jpg','https://i.redd.it/3n3lixsq5vq01.jpg','https://i.redd.it/xovz0z5mewq01.jpg','https://i.redd.it/kqsotjgj0yq01.jpg','http://images.memes.com/meme/868122','http://images.memes.com/meme/1452777','http://images.memes.com/meme/19242.jpg','http://images.memes.com/meme/1111179','https://i.redd.it/cva9tb3r1wq01.png','https://imgur.com/2hlsj7Q','https://i.redd.it/f5l79kk17yq01.jpg','https://i.redd.it/ii9w5dpqyxq01.jpg','https://imgur.com/UH6DABG','https://i.redd.it/5zo511n7bxq01.jpg','https://i.redd.it/dxefclltiyq01.jpg']
	secure_random = random.SystemRandom()
	m=secure_random.choice(list)
	embed = discord.Embed(description="Random Meme", color=0x00BFFF)
	embed.set_image(url=m)
	await client.say(embed=embed)



client.run("NDMyNjA3OTE0NDMyMTM1MTY5.DawDKA.RZ9zUBcfPrPmbOYHhsFw3XdByR0")
