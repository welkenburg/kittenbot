import discord
from discord.ext import tasks, commands
from os import listdir
import random

prefix = ";"

client = commands.Bot(command_prefix = prefix,activity=discord.Game(f'{prefix}help'),help_command=None)

class help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(help='Shows this message')
	async def help(self,ctx,cog=None):
		cogs = self.client.cogs.keys() if cog == None else [cog]
		for each in cogs:
			embed = discord.Embed(title=f"Help {each}",color = discord.Color(0x44FF44)) if each != 'help' else discord.Embed(title=f"Help",color = discord.Color(0x44FF44))
			for command in self.client.get_cog(each).get_commands():
				command_value = f'{self.client.command_prefix}{command.name}'
				for para in command.params:
					if '=' in str(command.params[para]):
						command_value += f' [{para}]'
					elif not para in ["self","ctx"]:
						 command_value += f' <{para}>'
				embed.add_field(name=f"`{command_value}`",value=f"{command.help}",inline=False)
			await ctx.send(embed=embed)

class test(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(help="Marque le salon comme occupé")
	@commands.has_permissions(administrator=True)
	async def close(self,ctx):
		if 'libre' in ctx.channel.name:
			await ctx.message.delete()
			await ctx.channel.edit(name=f"{'-'.join(ctx.channel.name.split('-')[:2])}-occupé")
			await ctx.send(f"Le salon est occupé")

	@commands.command(help="Marque le salon comme libre")
	@commands.has_permissions(administrator=True)
	async def open(self,ctx):
		if 'occupé' in ctx.channel.name:
			await ctx.message.delete()
			await ctx.channel.edit(name=f"{'-'.join(ctx.channel.name.split('-')[:2])}-libre")
			await ctx.send(f"Le salon a été libéré")

client.add_cog(test(client))
client.add_cog(help(client))

@client.event
async def on_ready():
	print('The bot is ready!')


client.run('')
