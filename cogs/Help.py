import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(
            title='คำสั่งของน้อนทั้งหมด',
            color=0xf77eff
        )
        embed.add_field(name='help', value='`ah help`')
        embed.add_field(name='fun', value='`ah help fun`')

        await ctx.send(embed=embed)
    
    @help.group()
    async def fun(self, ctx):
        embed = discord.Embed(
            title='Fun commands',
            color=0xf77eff,
            description='dick/penis meme/memes'
        )
        embed.add_field(name='usage', value='ah {commands}')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
