import discord
from discord.ext import tasks, commands

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

def setup(client):
	client.add_cog(test(client))
