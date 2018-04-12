import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import wikipedia


Client = discord.Client()
client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Bot is ready!")

def wiki_summary(arg):
	definition = wikipedia.summary(arg, sentences=1, chars=100, 
	auto_suggest=True, redirect=True)
	return definition	
		
		
@client.event
async def on_message(message):
	if message.content.upper().startswith('-SAY'):
		if message.author.id == "399567243744116738" or message.author.id == "293447483818901504" or message.author.id == "331876823443177473":
			args = message.content.split(" ")
			await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
			await client.delete_message(message)
		else:
			await client.send_message(message.channel, "You do not have the permissions to use that command!")
		
		
		

	if message.content.startswith('-kys'):
		await client.send_message(message.channel, "no u {0.author.mention}".format(message))
	    
	if message.content.upper().startswith('-RPS'):
		a=message.content[5:]
		answers = random.randint(1,3)
		if message.content[5:] =="":
			await client.send_message(message.channel, "Invalid, Choose rock/paper/scissors.")		
		elif answers == 1 and 'rock' in a: #rock
			await client.send_message(message.channel, "💎 | I choose *rock* too! It's a draaaw!")
		elif answers == 1 and 'paper' in a: #rock
			await client.send_message(message.channel, "💎 | I choose *rock*! You won and I lost...")	
		elif answers == 1 and 'scissors' in a: #rock
			await client.send_message(message.channel, "💎 | I choose *rock*! I won and you lost...")
			
		elif answers == 2 and 'rock' in a: #paper
			await client.send_message(message.channel, "📰 | I choose *paper*! I won and you lost...")
		elif answers == 2 and 'paper' in a: #paper
			await client.send_message(message.channel, "📰 | I choose *paper* too! It's a draaaw!")	
		elif answers == 2 and 'scissors' in a: #paper
			await client.send_message(message.channel, "📰 | I choose *paper*! You won and I lost...")
			
		elif answers == 3 and 'rock' in a: #scissors
			await client.send_message(message.channel, "✂ | I choose *scissors*! You won and I lost...")
		elif answers == 3 and 'paper' in a: #scissors
			await client.send_message(message.channel, "✂ | I choose *scissors*! I won and you lost...")	
		elif answers == 3 and 'scissors' in a: #scissors
			await client.send_message(message.channel, "✂ |I choose *scissors* too! It's a draaaw!")
		
		else:
			await client.send_message(message.channel, "Invalid, choose rock/paper/scissors.")	
			

			
			

	if message.content.upper().startswith('-8BALL'):
		if message.content[7:] =="":
			await client.send_message(message.channel, "🎱 | Missing required argument - question")
		else:
			ans = True
			while ans:
				answers = random.randint(1,8)
				if answers == 1:
					await client.send_message(message.channel, "🎱 | It is certain.")
					break
    
				elif answers == 2:
					await client.send_message(message.channel, "🎱 | Outlook good.")
					break
    
				elif answers == 3:
					await client.send_message(message.channel, "🎱 | You may rely on it.")
					break
    
				elif answers == 4:
					await client.send_message(message.channel, "🎱 | NO U!")
					break
    
				elif answers == 5:
					await client.send_message(message.channel, "🎱 | Concentrate and ask again.")
					break
    
				elif answers == 6:
					await client.send_message(message.channel, "🎱 | Reply hazy, try again.")
					break
    
				elif answers == 7:
					await client.send_message(message.channel, "🎱 | My reply is no.")
					break
    
				elif answers == 8:
					await client.send_message(message.channel, "🎱 | My sources say no.")
					break
		
		

	if message.content.upper().startswith('-FLIP'):
		a=message.content[5:]
		answers = random.randint(1,2)
		if message.content[5:] =="":
			await client.send_message(message.channel, "Invalid, Choose heads/tails")		
		elif answers == 1 and 'heads' in a: #heads
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Heads. \n\nNice guess!", inline=False)
			embed.set_thumbnail(url='http://www.thesaint-online.com/wp-content/uploads/2017/04/pound-coin-front.png')
			await client.send_message(message.channel, embed=embed)			
		elif answers == 1 and 'tails' in a: #heads
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Heads. \n\nBetter luck next time...", inline=False)
			embed.set_thumbnail(url='http://www.thesaint-online.com/wp-content/uploads/2017/04/pound-coin-front.png')
			await client.send_message(message.channel, embed=embed)
		elif answers == 2 and 'tails' in a: #tails
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Tails. \n\nNice guess!", inline=False)
			embed.set_thumbnail(url='https://www.chards.co.uk/media/blog/46/2008onepoundrev500.png')
			await client.send_message(message.channel, embed=embed)
		elif answers == 2 and 'heads' in a: #tails
			embed = discord.Embed(title=":moneybag: Coin Flip :moneybag:", description="", color=0x00ff00)
			embed.add_field(name="Result", value="It was Tails. \n\nBetter luck next time...", inline=False)
			embed.set_thumbnail(url='https://www.chards.co.uk/media/blog/46/2008onepoundrev500.png')
			await client.send_message(message.channel, embed=embed)	

		else:
			await client.send_message(message.channel, "Invalid, choose heads/tails.")
		
		
		
	if message.content.startswith('Hi'):
		await client.send_message(message.channel, "Hello {0.author.mention}!".format(message))
		
		
	if message.content.upper().startswith('-WIKI'):
		try:
			words = message.content.split()
			important_words = words[1:]
			embed = discord.Embed(title="", description="", color=0x00ff00)
			embed.add_field(name="According to Wikipedia:", value=wiki_summary(important_words))
			embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Wikipedia_svg_logo.svg/2000px-Wikipedia_svg_logo.svg.png')
			await client.send_message(message.channel, embed=embed)
		except:
			await client.send_message(message.channel, "Error. There were no results matching the query.")

		

		
client.run("NDMyNjA3OTE0NDMyMTM1MTY5.DawDKA.RZ9zUBcfPrPmbOYHhsFw3XdByR0")
