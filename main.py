import discord, aiosqlite
from discord.ext import commands, tasks


@tasks.loop(seconds=12) 
async def autopfp():  
    for guild in bot.guilds: 
       for member in guild.members:  
        if member.bot:
            continue
        else:
         if member.avatar:
          async with bot.db.cursor() as cursor:
            await cursor.execute("SELECT * FROM autopfp")
            results = await cursor.fetchall()
            for result in results:
             channel_id = result[1]
             user = await bot.fetch_user(member.id)
             embed = discord.Embed(color=0x2f3136, description="[our pinterest](https://www.pinterest.com/antipfps/)", timestamp=datetime.datetime.now())
             embed.set_image(url=user.avatar.url)
             embed.set_author(name="follow our pinterest", icon_url="https://images-ext-1.discordapp.net/external/patbltTGq126PE_DJ-ZVbxORqhW8cipRzo95lYr6FaE/%3Fsize%3D240%26quality%3Dlossless/https/cdn.discordapp.com/emojis/1026647994390552666.webp")
             embed.set_footer(text="powered by {}".format(bot.user.name))
             try:
              channel = bot.get_channel(channel_id)
              await channel.send(embed=embed)
              await asyncio.sleep(12)
             except:
                pass
    
 
@tasks.loop(seconds=12) 
async def autobanner():  
    for guild in bot.guilds: 
       for member in guild.members:  
        if member.bot:
            continue
        else:
         user = bot.fetch_user(member.id)
          async with bot.db.cursor() as cursor:
            await cursor.execute("SELECT * FROM autobanner")
            results = await cursor.fetchall()
            for result in results:
             channel_id = result[1]
             embed = discord.Embed(color=0x2f3136, description="[our pinterest](https://www.pinterest.com/antipfps/)", timestamp=datetime.datetime.now())
             embed.set_image(url=user.banner.url)
             embed.set_author(name="follow our pinterest", icon_url="https://images-ext-1.discordapp.net/external/patbltTGq126PE_DJ-ZVbxORqhW8cipRzo95lYr6FaE/%3Fsize%3D240%26quality%3Dlossless/https/cdn.discordapp.com/emojis/1026647994390552666.webp")
             embed.set_footer(text="powered by {}".format(bot.user.name))
             try:
              channel = bot.get_channel(channel_id)
              await channel.send(embed=embed)
              await asyncio.sleep(12)
             except:
                pass


class Bot(commands.AutoShardedBot):
  def __init__(self):
    super().__init__(
        command_prefix="?",
        intents=discord.Intents.all(),
        help_command=None
    ) 
    self.token = ""

  async def on_connect(self): 
    setattr(bot, "db", await aiosqlite.connect("main.db"))
    print("Attempting to connect to Discord's API")
    await self.load_extension("jishaku")
    for file in os.listdir("./cogs"): 
      if file.endswith(".py"):
        try: 
            await self.load_extension("cogs." + file[:-3])
            print("loaded extension {}".format(file[:-3])) 
        except Exception as e: 
           print("unable to load extension {} - {}".format(file[:-3], e))
  
  async def on_ready(self):
    autopfp.start()
    autobanner.start()
    print(f"logged in as {bot.user}")
    
bot = Bot()
bot.run(bot.token, reconnect=True)
