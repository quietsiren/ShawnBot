#shawnBot.py

# My UID: 119849158310887424

import os
import json
import random
import discord
from discord.utils import find
from discord.utils import get
from discord.ext import commands

# Read some sweet json files.
with open('auth.json') as auth_file:
    fd = json.load(auth_file)
    AUTH = fd['token']

with open('nine_nine.json') as nine_nine_file:
    fd = json.load(nine_nine_file)
    quote = fd['brooklyn_99_quotes']
    
with open('jokes.json') as joke_file:
    fd = json.load(joke_file)
    joke = fd['jokes']

with open('workgroups.json') as groups_file:
    fd = json.load(groups_file)
    groups = fd['groups']

def get_all_members_name(guild):
    for member in guild.member:
        yield member.name

'''

Discord BOT crap below this:

'''

bot = commands.Bot(
    command_prefix='!',
    case_insensitive=True
    )

bot.author_id = 119849158310887424

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You have no power here.')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    response = random.choice(quote)
    await ctx.send(response)

@bot.command(name='dad', help='Responds with a random dad joke')
async def dad_jokes(ctx):
    response = random.choice(joke)
    await ctx.send(response)

@bot.command(name='scatter', help='Moves all students to their Workgroup Voice Channels')
@commands.has_role('Instructor')
async def disperse(ctx):
    await ctx.send("SCATTER!!!!")

@bot.command(name='assemble', help='Moves all students from their Workgroup Voice Channels, back into General')
@commands.has_role('Instructor')
async def assemble(ctx):    
    await ctx.send("Students....Assemble in General.")

#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     print(existing_channel)

@bot.command(name='crank', help='You should know who he is...')
async def crank(ctx):
    await ctx.send("Do you know who he is?!")

@bot.command(name='shawn', help='He\'s the kitty, the very bestest kitty.')
async def shawn(ctx):
    await ctx.send("KITTEH!!!")

@bot.command(name='restart', help='Take a catnap')
async def restart(ctx):
    await ctx.send("Yaawwwn")
    await ctx.logout()
    # await ctx.login(AUTH, bot=True)

bot.run(AUTH)