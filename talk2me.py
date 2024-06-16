import discord
from discord import app_commands
from discord.ext import commands
import google.generativeai as palm
import os


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix='', intents=discord.Intents.default())

print(os.environ)

api_key = os.environ["api_key"]
client_key = os.environ["client_key"]



palm.configure(api_key=api_key)

@client.command(name = "hello", description = "My first application Command") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message(f"Hello! {interaction.user.mention}")

@client.command(name = "test", description = "My second application Command") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def second_command(interaction):
    await interaction.response.send_message("testing...")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    content = message.content
    print(content)
    response = palm.chat(prompt=[content], model = "models/chat-bison-001")
    print(response)
    await message.channel.send(response.last[0:2000])
    response.reply(content)

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

# Run the bot
client.run(client_key)

