#
#	Billy-Bot made for our discord server. (Version: 0.1 - Alpha)
#	Made by YungBender#7283
#
# -*- coding: utf-8 -*-

import discord # Discord API
import asyncio # await, async function
import random # RNG generator
import libs.billy_functions # importing other billy function

client = discord.Client()

@client.event # Logging to discord server
async def on_ready():
	print ("Logged in as")
	print (client.user.name)
	print (client.user.id)
	print ("--------------")

@client.event
async def on_message(message): # Checks users message

	if message.content.startswith("!flip"): # User selected flip -- prints true or false
		result = random.choice([True, False])
		await client.send_message(message.channel, result)

	#elif message.content.startswith("!quote"): # User selected quote
		#result = random.

	elif message.content.startswith("!introduce") or message.content.startswith("!help") or message.content.startswith("!commands"): # User selected help message
		result = "```	\t\t\tMy name is Billy Herrington, aniki. (BILLY-BOT 0.1 Alpha)\nCommands: \n\t!flip - returns true or false for question \n\t!pick - picks one word from your input \n\t!quote - like embarrassing me huh? \n\t\tMade by YungBender#7283	\nTHANK YOU SIR \n ```"
		await client.send_message(message.channel, result)

	elif message.content.startswith("!pick"): # User selected pick -- billy answers random word from users input
		result = message.content[5:]
		result = billy_functions.get_word(result)
		await client.send_message(message.channel, result)

	elif message.content.startswith("!roll"): # User selected roll -- billy answers random number from 0 to number #max
		max = message.content[5:]
		max = int(max)
		result = random.randint(0,max)
		await client.send_message(message.channel, result)

	elif message.content.startswith("!rng"): # User selected rng -- billy answers random number generated from 0 to 32768
		result = random.randint(0,32768)
		await client.send_message(message.channel, result)

client.run("NDQ4ODIwMTM5NjQzODk1ODE5.Deb_qQ.lF2-AlXAuKv1Hv_gan6YyjogUbY")