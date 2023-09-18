from twitchio.ext import commands, routines
import twitchio
from config import ACCESS_TOKEN, CLIENT_ID
import random


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix='!', initial_channels=['kh1rsan', 'stammer_pss'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
    
    @commands.cooldown(rate=1, per=3, bucket=commands.Bucket.channel)
    @commands.command()
    async def chatters(self, ctx: commands.Context):
        await ctx.send(f'{ctx.chatters.copy().pop().name}')

    @commands.cooldown(rate=1, per=3, bucket=commands.Bucket.channel)
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Приветики, @{ctx.author.display_name}!')
    
    @commands.cooldown(rate=1, per=3, bucket=commands.Bucket.channel)
    @commands.command()
    async def лапочка(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.display_name}, ты лапочка на {random.randint(0, 100)}%! SeemsGood')
    
    @commands.cooldown(rate=1, per=3, bucket=commands.Bucket.channel)
    @commands.command()
    async def вредность(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.display_name} вредина на целых {random.randint(0, 100)}%! ;p')

    @commands.cooldown(rate=1, per=3, bucket=commands.Bucket.channel)
    @commands.command()
    async def мяу(self, ctx: commands.Context):
        await ctx.send(f'Вот что я умею: !кусь(кому) !лапочка !вредность')

    @commands.cooldown(rate=1, per=3, bucket=commands.Bucket.channel)
    @commands.command()
    async def кусь(self, ctx: commands.Context):
        message:str = ctx.message.content
        message = message.replace("!кусь", '')
        
        await ctx.send(f"@{ctx.author.display_name} делает кусь {message.lstrip() if message != '' else 'своему мягкому месту'}! PopNemo ")
    

bot = Bot()
bot.run()




