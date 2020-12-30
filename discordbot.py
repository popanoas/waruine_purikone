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
ID_ROLE_WELCOME = 666361330827132979 # わるいねのID

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

@tasks.loop(seconds=60)
async def totuDeclaration():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
  
        #ランドソル杯データ入力
        #channel = client.get_channel(ID_Mana)
        #msg = await channel.send('日付が変わりました！記入が終わったらリアクションを付けてね♡ \n https://docs.google.com/spreadsheets/d/1nCdtFHS-60WcRZDx8hTXHFm3mPuEqefntQxeRfM2Lv0/edit#gid=632518118')  
        #await msg.add_reaction(ID_emoji)
        
loop.start()          
    
client.run(token)
