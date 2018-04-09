import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random

from datetime import datetime, timezone


attr = []

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
	print ("Ready when you are!")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)


@bot.event
async def on_message(message):
	if message.content.upper().startswith('-RPS'):
		a=message.content[5:]
		answers = random.randint(1,3)
		if message.content[5:] =="":
			await bot.send_message(message.channel, "Invalid, Choose rock/paper/scissors.")		
		elif answers == 1 and 'rock' in a: #rock
			await bot.send_message(message.channel, "I choose rock. \n" + "It's a Draw.")
		elif answers == 1 and 'paper' in a: #rock
			await bot.send_message(message.channel, "I choose rock. \n"+ "You Won.")	
		elif answers == 1 and 'scissors' in a: #rock
			await bot.send_message(message.channel, "I choose rock. \n" + "You Lost.")
			
		elif answers == 2 and 'rock' in a: #paper
			await bot.send_message(message.channel, "I choose paper. \n" + "You Lost.")
		elif answers == 2 and 'paper' in a: #paper
			await bot.send_message(message.channel, "I choose paper. \n" + "It's a Draw.")	
		elif answers == 2 and 'scissors' in a: #paper
			await bot.send_message(message.channel, "I choose paper. \n" + "You Won.")
			
		elif answers == 3 and 'rock' in a: #scissors
			await bot.send_message(message.channel, "I choose scissors. \n" + "You Won.")
		elif answers == 3 and 'paper' in a: #scissors
			await bot.send_message(message.channel, "I choose scissors. \n" + "You Lost.")	
		elif answers == 3 and 'scissors' in a: #scissors
			await bot.send_message(message.channel, "I choose scissors. \n" + "It's a Draw")
		
		else:
			await bot.send_message(message.channel, "Invalid, choose rock/paper/scissors.")			

			

bot.run("NDMyNjA3OTE0NDMyMTM1MTY5.DawDKA.RZ9zUBcfPrPmbOYHhsFw3XdByR0")
