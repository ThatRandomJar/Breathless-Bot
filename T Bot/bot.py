import discord
import os
from discord import Permissions
from discord.ext import commands
import random
from discord.ext.commands import has_role
from discord.ext.commands import has_guild_permissions
from discord.ext.commands import CheckFailure
from keep_alive import keep_alive


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['speak'])
async def _speak(ctx, *, statement):
    embedVar = discord.Embed(title=statement)
    await clear(ctx, 1)
    await ctx.send(embed = embedVar)

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    embedVar = discord.Embed(title="GTFO", description=f'{member} has been kicked..', color=0x00ff00)
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
    embedVar = discord.Embed(title="GTFO", description=f'{member} has been banned..', color=0x00ff00)
    await member.ban(reason = reason)

@client.command()
@has_guild_permissions(manage_roles = True)
async def mute(ctx, member: discord.Member, *, reason = None):
    
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    try:
        await member.add_roles(role)
    except Exception as e:
        await ctx.send('Cannot assign role. Error: ' + str(e))
        
    serverName = member.guild.name
    embed = discord.Embed(title="User Muted!", description=f"**{member}** was muted Reason: {reason}".format(member), color=0x008000)
    content = discord.Embed(title="User Muted!", description=f"You were muted in {serverName} Server for {reason}".format(member), color=0xff00f6)
    await ctx.send(embed=embed)
    await member.send(embed = content)

@mute.error
async def mute_error(error, ctx):
    if isinstance(error, CheckFailure):
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
        await ctx.send(embed=embed)
    else:
        await ctx.send("unknown error")

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Not really.",
                 "Yes.",
                 "Signs point to yes.",
                 "Not in the mood rn, ask later.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Yesn't",
                 "Very doubtful."]
    embedVar = discord.Embed(title="Tile", description=responses, color=0x00ff00)
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
client.run(os.environ.get['DISCORD_BOT_SECRET'])