import discord, aiohttp, datetime, random, random, asyncio, traceback
from discord.ext import commands, tasks 
from io import BytesIO


class autopost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.Cog.listener()
    async def on_ready(self):
      async with self.bot.db.cursor() as cursor: 
        await cursor.execute("CREATE TABLE IF NOT EXISTS autopfp (guild_id INTEGER, channel_id INTEGER)")
        await cursor.execute("CREATE TABLE IF NOT EXISTS autobanner (guild_id INTEGER, channel_id INTEGER)")
      await self.bot.db.commit() 
    

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def autopfp(self, ctx: commands.Context, decide: str=None, channel: discord.TextChannel=None):
      if not ctx.author.guild_permissions.manage_guild:
        embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} you are missing permissions `manage_guild`") 
        await ctx.reply(embed=embed, mention_author=False)
        return 
      if decide == None:
        embed = discord.Embed(color=0x2f3136, description=f"`syntax: autopfp add [channel]`") 
        await ctx.reply(embed=embed, mention_author=False)  
        return 
      if decide == "add" and channel == None:
        embed = discord.Embed(color=0x2f3136, description=f"`syntax: autopfp add [channel]`") 
        await ctx.reply(embed=embed, mention_author=False) 
        return 
      elif decide == "add" and channel != None:
       async with self.bot.db.cursor() as cursor: 
        await cursor.execute("SELECT * FROM autopfp WHERE guild_id = {}".format(ctx.guild.id))
        check = await cursor.fetchone()
        if check is None:
         url = self.bot.user.avatar.url   
         async with aiohttp.ClientSession() as ses: 
           async with ses.get(url) as r:
            try:
             if r.status in range (200, 299):
                img = BytesIO(await r.read())
                bytes = img.getvalue()
                await cursor.execute("INSERT INTO autopfp VALUES (?, ?)", (ctx.guild.id, channel.id))
                await self.bot.db.commit()
                embe = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} added autopfp channel to {channel.mention}")
                await ctx.reply(embed=embe, mention_author=False)
                return
             else:
                embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} failed to add autopfp channel")
                await ctx.reply(embed=embed, mention_author=False)
            except:
             embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} failed to add autopfp channel")
             await ctx.reply(embed=embed, mention_author=False)
        elif check is not None:
         embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} autopfp channel is already added, please remove it before adding a new one")
         await ctx.reply(embed=embed, mention_author=False)
         return 
      elif decide == "remove":
       async with self.bot.db.cursor() as cursor:  
        await cursor.execute("SELECT * FROM autopfp WHERE guild_id = {}".format(ctx.guild.id))
        check = await cursor.fetchone()
        if check is None: 
         embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} autopfp channel isn't added")
         await ctx.reply(embed=embed, mention_author=False)
         return  
        elif check is not None:   
          await cursor.execute("DELETE FROM autopfp WHERE guild_id = {}".format(ctx.guild.id))
          await self.bot.db.commit()
          e = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} autopfp channel removed")
          await ctx.reply(embed=e, mention_author=False)
          return
    
    
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def autobanner(self, ctx: commands.Context, decide: str=None, channel: discord.TextChannel=None):
      if not ctx.author.guild_permissions.manage_guild:
        embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} you are missing permissions `manage_guild`") 
        await ctx.reply(embed=embed, mention_author=False)
        return 
      if decide == None:
        embed = discord.Embed(color=0x2f3136, description=f"`syntax: autobanner add [channel]`") 
        await ctx.reply(embed=embed, mention_author=False)  
        return 
      if decide == "add" and channel == None:
        embed = discord.Embed(color=0x2f3136, description=f"`syntax: autobanner add [channel]`") 
        await ctx.reply(embed=embed, mention_author=False) 
        return 
      elif decide == "add" and channel != None:
       async with self.bot.db.cursor() as cursor: 
        await cursor.execute("SELECT * FROM autobanner WHERE guild_id = {}".format(ctx.guild.id))
        check = await cursor.fetchone()
        if check is None:
         url = self.bot.user.avatar.url   
         async with aiohttp.ClientSession() as ses: 
           async with ses.get(url) as r:
            try:
             if r.status in range (200, 299):
                img = BytesIO(await r.read())
                bytes = img.getvalue()
                await cursor.execute("INSERT INTO autobanner VALUES (?, ?)", (ctx.guild.id, channel.id))
                await self.bot.db.commit()
                embe = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} added autobanner channel to {channel.mention}")
                await ctx.reply(embed=embe, mention_author=False)
                return
             else:
                embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} failed to add autobanner channel")
                await ctx.reply(embed=embed, mention_author=False)
            except:
             embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} failed to add autobanner channel")
             await ctx.reply(embed=embed, mention_author=False)
        elif check is not None:
         embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} autobanner channel is already added, please remove it before adding a new one")
         await ctx.reply(embed=embed, mention_author=False)
         return 
      elif decide == "remove":
       async with self.bot.db.cursor() as cursor:  
        await cursor.execute("SELECT * FROM autobanner WHERE guild_id = {}".format(ctx.guild.id))
        check = await cursor.fetchone()
        if check is None: 
         embed = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} autobanner channel isn't added")
         await ctx.reply(embed=embed, mention_author=False)
         return  
        elif check is not None:   
          await cursor.execute("DELETE FROM autobanner WHERE guild_id = {}".format(ctx.guild.id))
          await self.bot.db.commit()
          e = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} autobanner channel removed")
          await ctx.reply(embed=e, mention_author=False)
          return
    
      
async def setup(bot) -> None:
    await bot.add_cog(autopost(bot))
