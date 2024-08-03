import os
import discord
import requests
import base64
from discord.ext import commands

token = ""
os.mkdir(os.path.join(os.path.dirname(__file__), r"\guilds")) if not os.path.exists(os.path.join(os.path.dirname(__file__), r"\guilds")) else print()
client = commands.Bot(command_prefix="!")

@client.command()
async def backupguild(ctx):
    os.mkdir(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}")) if not os.path.exists(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}")) else print()
    try:
        open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\server.json"), "x") 
    except FileExistsError:
        pass
    server = []
    channels = []
    roles = []
    for ch in ctx.guild.text_channels:
        channels.append(
            {
                "name": ch.name,
                "id": ch.id,
                "type": "text",
                "desc": ch.description
            }
        )
    for ch in ctx.guild.voice_channels:
        channels.append(
            {
                "name": ch.name,
                "id": ch.id,
                "type": "vc",
                "desc": ch.description
            }
        )
    for rl in ctx.guild.roles:
        roles.append(
            {
                "name": rl.name,
                "id": rl.id,
                "perms_int": rl.permissions.value 
            }
        )
    metadata = {
        "name": ctx.guild.name,
        "desc": ctx.guild.description,
        "icon": str(base64.b64encode(bytes(requests.get(ctx.guild.icon).text, encoding="utf-8")))
    }
    server.append(
        {
            "metadata": metadata,
        }
    )
    server.append(
        {
            "channels": channels,
        }
    )
    server.append(
        {
            roles
        }
    )
    try:
        open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\icon.png"), "x") 
    except FileExistsError:
        pass
    with open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\icon.png"), "wb") as f:
        f.write(bytes(base64.b64decode(metadata["icon"])))
    with open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\server.json"), "w") as f:
        f.write(str(server))
    os.mkdir(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\stickers")) if not os.path.exists(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\stickers")) else print()
    os.mkdir(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\emoji")) if not os.path.exists(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\emoji")) else print()
    for sticker in ctx.guild.stickers:
        try:
            open(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\stickers"), f"\{sticker.name}.gif"), "x")
        except FileExistsError:
            pass
        with open(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\stickers"), f"\{sticker.name}.gif"), "wb") as f:
            f.write(bytes(requests.get(f"https://media.discordapp.net/stickers/{sticker.id}.png"), encoding="utf-8"))
    for emoji in ctx.guild.emojis:
        try:
            open(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\emojis"), f"\{emoji.name}.gif"), "x")
        except FileExistsError:
            pass
        with open(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\emojis"), f"\{emoji.name}.gif"), "wb") as f:
            f.write(bytes(requests.get(f"https://media.discordapp.net/emojis/{emoji.id}.png"), encoding="utf-8"))

@client.command()
async def savemsgs(ctx):
    os.mkdir(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}")) if not os.path.exists(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}")) else print()
    os.mkdir(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages")) if not os.path.exists(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages")) else print()
    for channel in ctx.guild.text_channels:
        try:
            open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages"), f"\messages-{channel.name}.json", "x")
        except FileExistsError:
            pass
        with open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages"), f"\messages-{channel.name}.json", "w") as f:
            messages = []
            for msg in ctx.channel.messages:
                attachments = []
                for attachment in msg.attachments:
                    attachments.append(attachment.filename)
                messages.append(
                    {
                        "author_dsp": msg.author.display_name,
                        "author_usr": msg.author.name,
                        "author_id": msg.author.id,
                        "sent_at": msg.created_at,
                        "content": msg.content,
                        "attachments": attachments,
                    }
                )
                if attachments != []:
                    os.mkdir(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages"), r"\attachments")) if not os.path.exists(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages"), r"\attachments")) else print()
                    for attachment in ctx.message.attachments:
                        await attachment.save(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), r"\guilds"), f"\{ctx.guild.id}"), r"\messages"), r"\attachments"), f"\{attachment.filename}"))
#end of work for today 03/08/2024 18:20 UTC (DD/MM/YYYY)

client.run(token)