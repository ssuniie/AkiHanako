import discord
from discord.ext import commands


class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['donate'])
    async def support(self, ctx):
        embed = discord.Embed(
            title='สนับสนุนค่าขนมน้อน',
            color=0xf77eff
        )
        embed.add_field(
            name='Ko-Fi',
            value='[https://ko-fi.com/ssuniie](https://ko-fi.com/ssuniie)'
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Support(client))
