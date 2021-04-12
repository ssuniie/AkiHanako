import discord
from discord.ext import commands

import os

# ! Intents Setting
intents = discord.Intents.all()

# * Client Information
client = commands.Bot(
    command_prefix='ah ',
    intents=intents,
    case_insensitive=True
)
TOKEN = os.environ['CLIENT_TOKEN']

# * remove commands from client.
client.remove_command('help')


# Reload Cogs
@client.command()
@commands.is_owner()
@commands.dm_only()
async def reload(ctx, extension):
    if extension.endswith('.py'):
        client.unload_extension(f'cogs.{extension[:-3]}')
        client.load_extension(f'cogs.{extension[:-3]}')
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')

    await ctx.send(f'cogs.{extension} reloaded!')
    print(f'cogs.{extension} reloaded!')


# ! Load all Cogs file
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'cogs.{filename[:-3]} loaded!')


# ! run the client / Required TOKEN
client.run(TOKEN)
