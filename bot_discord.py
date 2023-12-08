import discord
from discord.ext import commands
import os

# два класса: Bot и Client

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
TOKEN = 'MTE3NjQ4NzkzOTY1NjY1MDgwMg.Ge6sVy.Lfqly_NAeMN0t_r4BPS42mprFjcQGHmWsUhV18'

items = {
    'бумага': '2-5 месяцев',
    'бутылка': '400 лет',
    'кожура': '2-5 недель'
}

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} запущен!')

@bot.command()
async def send_message_hello(ctx):
    await ctx.send('hello')

@bot.command()
async def echo_bot(ctx):
    await ctx.reply(ctx)

@bot.command()
async def decomp(ctx, item):
    if item in items:
        time_to_decomp = items[item]
        await ctx.send(f'Предмет {item} разлагается примерно {time_to_decomp}')
    else:
        await ctx.send('По такому предмету пока нет информации')

@bot.command()
async def sort(ctx, item):
    if item == 'батарейки':
        await ctx.send('Отдать на переработку')
    elif item == 'стекло':
        await ctx.send('Отдать на переработку, можно выбросить в специальную урну')
    else:
        await ctx.send('По такому предмету пока нет информации')


bot.run(TOKEN)
