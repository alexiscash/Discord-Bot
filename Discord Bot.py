import discord
from discord.ext import commands
import asyncio
import logging
import json

with open('auth.json') as f:
    token = json.load(f)
    f.close()

with open('package.json') as p:
    package = json.load(p)
    p.close()



logging.basicConfig(level=logging.ERROR)


Client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print ("Ya boi is ready.")

@client.event
async def on_message(message):
    if (message.content.lower() == "help"):
        await client.send_message(message.channel, 'Hi! I am Bot Boi. The boi who is a bot. \n\n !say: say something \n !tell: @person say something')
    elif ('rose' in message.content):
        try:   
            await client.add_reaction(message, u"\U0001F339")
        except discord.errors.HTTPException:
            await client.send_message(message.channel, 'Yeah idk what that is bro')
    elif (message.content == "swag"):
        await client.send_message(message.channel, 'Hell yeah swag boi')
    elif (message.content.lower().startswith('!say')):
        args = message.content.split()
        await client.send_message(message.channel, "%s" % (' '.join(args[1:])))
    elif (message.content.lower().startswith('!tell')):
        args = message.content.split()
        await client.send_message(message.channel, "<%s> %s" % (args[1], ' '.join(args[2:])), tts=True)
    elif (message.content == "ur mom gay"):
        await client.send_message(message.channel, "no u")
    elif (message.content == "Your mother is a"):
        await client.send_message(message.channel, "whore")

    if (message.content.lower().startswith('!greet')):
        await client.send_message(message.channel, 'Fuck you')
        msg = await client.wait_for_message(author=message.author, content='fuck you too')
        await client.send_message(message.channel, 'I like that')
        

          

client.run(token['token'])
