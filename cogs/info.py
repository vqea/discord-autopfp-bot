import discord, time, datetime, asyncio
from discord.ext import commands
from typing import Union

global startTime

class info(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_connect(self):
        global startTime
        startTime = time.time()
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def uptime(self, ctx):
     uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
     e = discord.Embed(color=0x2f3136, description=f"**{self.bot.user.name}'s** uptime: **{uptime}**")
     await ctx.reply(embed=e, mention_author=False)
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user) 
    async def ping(self, ctx):
        await ctx.reply(f"...pong :ping_pong:`{round(self.bot.latency * 1000)}ms`", mention_author=False)
        
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help(self, ctx: commands.Context, *, cmd=None):
     if cmd is None:
        e = discord.Embed(color=0x2f3136, title="help commands") 
        e.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        e.add_field(name=f"{self.bot.user.name}+", value="`autopfp`, `autobanner`", inline=False)
        e.add_field(name="info", value="`ping`, `uptime`", inline=False)
        e.set_footer(text=f"{len(self.bot.commands)} commands")
        e.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.reply(embed=e, mention_author=False) 

async def setup(bot):
    await bot.add_cog(info(bot))
