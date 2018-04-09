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
	embed = discord.Embed(description="Avatar", color=0x00BFFF)
	embed.set_image(url=user.avatar_url)
	await client.say(embed=embed)
	
	
	
@client.command(pass_context=True)
async def multi(ctx, a,b):
	c=int(a) * int(b)
	s=str(c)
	await client.say(a + " * " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
async def sub(ctx, a,b):
	c=int(a) - int(b)
	s=str(c)
	await client.say(a + " - " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
async def add(ctx, a,b):
	c=int(a) + int(b)
	s=str(c)
	await client.say(a + " + " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
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
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await client.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description=':ping_pong: Pong! `{}miliseconds`'.format(round((t2-t1)*1000)), color=0x2874A6)
	await client.say(embed=embed)



client.run("NDMyNjA3OTE0NDMyMTM1MTY5.DawDKA.RZ9zUBcfPrPmbOYHhsFw3XdByR0")
