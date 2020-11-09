from discord.ext import commands
import discord
import asyncio
import os
intents=discord.Intents.all()
intents.typing = False
import traceback
import random
from datetime import datetime
from discord.ext import tasks
import threading

token = os.environ['DISCORD_BOT_TOKEN']


# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

ID_CHANNEL_README = 768272323341320232 #readmeチャンネルのID
ID_ROLE_WELCOME = 666361330827132979 # 当月クランメンバーのID

@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    if channel.id != ID_CHANNEL_README:
        return

    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    role = guild.get_role(ID_ROLE_WELCOME)

    await member.add_roles(role)
    msg = await channel.send('ようこそ！' + member.name + 'さん！')
    await asyncio.sleep(5) 
    await msg.delete()    

client.run(token)
