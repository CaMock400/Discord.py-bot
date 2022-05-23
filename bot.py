import discord
import random

intents = discord.Intents.default()
intents.members = True
client = discord.Client(case_insensetive=True, intents=intents, command_prifix="!")

def random_fact(): # just a feature
    liste = []
    with open('facts', 'r') as file:
        for line in file:
            liste.append(str(line))
    ran_liste = random.choice(liste)
    return ran_liste 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                           name='https://fridaysforfuture.de/ortsgruppen/holzkirchen/'))

@client.event
async def on_raw_reaction_add(payload): # for reaction role when sb posts a reaction 
    message_id = payload.message_id
    if message_id == "": # Message ID as  Int TODO
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "germanzero":
            role = discord.utils.get(guild.roles, name="germanzero")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload): # for reaction role when sb retracts a reaction
    message_id = payload.message_id
    if message_id == "": # Message ID as  Int TODO 
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "germanzero":
            role = discord.utils.get(guild.roles, name="germanzero")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
            else:
                pass
        else:
            pass

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Welcome Text")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", url=f"{member.avatar_url}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    channel = member.guild.get_channel(943247312019402792)
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.content.lower() == 'hi' == 'hallo':
        await message.channel.send(f'Hallo!')
    if message.content.lower() == '!fact':
        await message.channel.send(random_fact())
    if message.content.lower() == 'tschüss' or message.content == 'chiao':
        await message.channel.send('Tschüss!')
    if message.content.lower() == "!webseite":
        await message.channel.send('website')
    if message.content.lower() == "":# Like you want
        await message.channel.send()# Like you want
    if message.content.lower() == '!help':
        await message.channel.send()# Like you want
    if message.content.lower() == '!code':
        await message.channel.send()# Like you want
    if message.content.lower() == '!creator':
        await message.channel.send("CaMock400")
    if message.content.lower() == '!join':
        await message.channel.send("")# Like you want




client.run()#Your TOKEN TODO
