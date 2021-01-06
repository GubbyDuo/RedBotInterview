#Importing libraries
import discord
import json
import os
from redbot.core import commands
from redbot.core import Config
from discord.ext.commands import has_permissions

#The main class
class Mycog(commands.Cog):
	"""My cog class"""
	#This line makes sure it's looking in the right directory
	os.chdir('E:\Discord\RedInterview\Cogs\InterviewCog')
	print(os.getcwd())

	#The 'say' command.
	@commands.command()
	async def say(self, ctx, channel: discord.TextChannel, message: str = 'message'):
	"""This is the say command, it repeats what the users says in the channel they choose."""
	#I wanted to put this block of code into a seperate function but it wasn't letting me
	#This code chunk makes sure the author isn't on the blacklist
		authorid = ctx.message.author.id

		with open("./data/userdata.json", "r") as f:
			data = json.load(f)
			"""This loads the data from a JSON file"""
			for id in data:
				if authorid == id:
					return
		#If the author is not on the blacklist, it sends the message
		await channel.send(message)
		"""This sends the message after the checks are complete"""
	
	@commands.command()
	@has_permissions(manage_messages=True)
	async def blacklistuser(self, ctx, user: discord.User):
		"""The blacklist user command, this command will add the specified user to the blacklist, if the author has manage message perms"""
		authorid = ctx.message.author.id

		with open("./data/userdata.json", "r") as f:
			data = json.load(f)
			"""Once again, this loads data from the JSON file"""

			for id in data:
				if authorid == id:
					return

			data.append(user.id)

		with open("./data/userdata.json", "w") as f:
			json.dump(data, f, indent = 1)
			"""This code writes to the JSON file, instead of grabbing data"""

		await ctx.send("User " + user.name + " has been blacklisted!")
		"""This sends the message confirming a user was added to the blacklist"""