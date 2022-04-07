import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "fn!")

@client.event
async def on_ready():
	print("Bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
	await ctx.send("Hi! this is new bot and a basic one....features coming soon")

client.run("OTYwOTExNjQ5NTg4NTIzMDE4.YkxUtg.1rpp4uVPQ5tLtIR2MZ5GC05cI3E")