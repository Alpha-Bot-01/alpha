import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Bot is ready!")
				
		
		
@client.event
async def on_message(message):
	if message.content.upper().startswith('-SAY'):
		if message.author.id == "399567243744116738" or message.author.id == "293447483818901504" or message.author.id == "331876823443177473":
			args = message.content.split(" ")
			await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
			await client.delete_message(message)
		else:
			await client.send_message(message.channel, "You do not have the permissions to use that command!")
			


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
					await client.send_message(message.channel, "🎱 | NO U.")
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
		
		


		
		
		
		
		
		
		
		
		

		
client.run("NDMyNjA3OTE0NDMyMTM1MTY5.DawDKA.RZ9zUBcfPrPmbOYHhsFw3XdByR0")