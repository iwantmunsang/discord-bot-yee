import discord
from discord import client 
token = "OTAwNjk1OTI3MDAwNTYzODEy.YXFEcw.hfYBSsjt188SvHSd0jRMWllOExI"
clinent = discord.client()

@client._event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("=======================")

if message.content.startswith("!청소"):
    number = ing(message.content.split(" ")[1])
    await message.delete()
    await message.content.purge(limit=number)
    await message.content.send(f"{number}개의 메세지 삭제 완료!")

client.run("OTAwNjk1OTI3MDAwNTYzODEy.YXFEcw.hfYBSsjt188SvHSd0jRMWllOExI")