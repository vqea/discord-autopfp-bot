import discord 
from discord.ext import commands 

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content == f"<@{self.bot.user.id}>":
            await message.reply(f"prefix: `{self.bot.command_prefix}`")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): 
       if isinstance(error, commands.CommandNotFound):
        return 
       else:   
        e = discord.Embed(color=0x2f3136, description=f"{ctx.author.mention} {error}")
        await ctx.reply(embed=e, mention_author=False)            

async def setup(bot):
    await bot.add_cog(events(bot))   
