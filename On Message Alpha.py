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
		
		
		

	if message.content.upper().startswith('-RPS'):
		a=message.content[5:]
		answers = random.randint(1,3)
		if message.content[5:] =="":
			await client.send_message(message.channel, "Invalid, Choose rock/paper/scissors.")		
		elif answers == 1 and 'rock' in a: #rock
			await client.send_message(message.channel, "I choose rock. \n" + "It's a Draw.")
		elif answers == 1 and 'paper' in a: #rock
			await client.send_message(message.channel, "I choose rock. \n"+ "You Won.")	
		elif answers == 1 and 'scissors' in a: #rock
			await client.send_message(message.channel, "I choose rock. \n" + "You Lost.")
			
		elif answers == 2 and 'rock' in a: #paper
			await client.send_message(message.channel, "I choose paper. \n" + "You Lost.")
		elif answers == 2 and 'paper' in a: #paper
			await client.send_message(message.channel, "I choose paper. \n" + "It's a Draw.")	
		elif answers == 2 and 'scissors' in a: #paper
			await client.send_message(message.channel, "I choose paper. \n" + "You Won.")
			
		elif answers == 3 and 'rock' in a: #scissors
			await client.send_message(message.channel, "I choose scissors. \n" + "You Won.")
		elif answers == 3 and 'paper' in a: #scissors
			await client.send_message(message.channel, "I choose scissors. \n" + "You Lost.")	
		elif answers == 3 and 'scissors' in a: #scissors
			await client.send_message(message.channel, "I choose scissors. \n" + "It's a Draw")
		
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
