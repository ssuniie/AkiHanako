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
        embed.add_field(name='Help', value='`ah help`')
        embed.add_field(name='Fun', value='`ah help fun`')
        embed.add_field(name='Mod', value='`ah help mod`')

        await ctx.send(embed=embed)
    
    @help.group()
    async def fun(self, ctx):
        embed = discord.Embed(
            title='Fun commands',
            color=0xf77eff,
            description='`ping dick/penis meme/memes`'
        )
        embed.add_field(name='การใช้งาน', value='ah {commands}')
        embed.add_field(name='ดูคำสั่งแบบละเอียด', value='ah help {commands}')

        await ctx.send(embed=embed)

    @help.group()
    async def mod(self, ctx):
        embed = discord.Embed(
            title='Mod Commands',
            color=0xf77eff,
            description='`thanos kick ban unban`'
        )
        embed.add_field(name='การใช้งาน', value='ah {commands}')
        embed.add_field(name='ดูคำสั่งแบบละเอียด', value='ah help {commands}')

        await ctx.send(embed=embed)

    @help.group()
    async def thanos(self, ctx):
        embed = discord.Embed(
            title='Thanos Command',
            color=0xf77eff,
            description='ดีดนิ้วแล้วปิดไมค์ไปครึ่งห้อง (ระยะเวลาปกติคือ 20 วินาที)'
        )
        embed.add_field(name='การใช้งาน', value='ah thanos {ระยะเวลา(วินาที)}')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
