import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
print(discord_token, flush=True)
discord_guild = os.getenv('DISCORD_GUILD')
print(discord_guild, flush=True)
discord_channel = os.getenv('DISCORD_CHANNEL')
print(discord_channel, flush=True)

client = discord.Client()

interest_roles = []

@client.event
async def on_ready():
    guild = client.get_guild(int(discord_guild))
    print(f'{client.user.name} has connected to guild {guild.name}, id {guild.id}', flush=True)
    for role in guild.roles:
        print(f'{role.name}: {role.colour}', flush=True)
        if role.colour == discord.Colour.orange():
            interest_roles.append(role)

    print('Interest Roles:', flush=True)
    for role in interest_roles:
        print(role.name, flush=True)

@client.event
async def on_message(message):
    guild = client.get_guild(int(discord_guild))
    channel = discord.utils.find(lambda c: c.name == discord_channel, guild.text_channels) 
    if message.channel == channel:
        response = discord.Embed()
        if message.content == 'rolecount':
            response.title = "Interest Role Counts"
            for role in interest_roles:
                count = len(role.members)
                response.add_field(name=role.name, value=count)
            await message.channel.send(content=None, embed=response)
        elif message.content == 'rolenames':
            response.title = "Interest Role User Lists"
            for role in interest_roles:
                value_string = ""
                for member in role.members:
                    value_string += f'{member.display_name}\n'
                response.add_field(name=role.name, value=value_string)
            await message.channel.send(content=None, embed=response)
    

client.run(discord_token)
