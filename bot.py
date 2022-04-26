import os
from twitchio.ext import commands

bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.command(name='warn')
async def warn(ctx, name):
    bads = open("bad names list.txt", "a")
    badsDict = {}
    bads.write(name)
    bads.write("\n")
    bads.close()
    bads = open("bad names list.txt", "r")
    bads.readlines
    for user in bads:
        user = user.strip()
        user = user.lower()
        if user in badsDict:
            badsDict[user]+=1
        else:
            badsDict[user]=1

    await ctx.send(f"@{name}, you are being warned. You have been warned {badsDict[name]} time(s).")


@bot.command(name='numwarn')
async def numwarn(ctx, name):
    badsDict = {}
    bads = open("bad names list.txt", "r")
    bads.readlines
    for user in bads:
        user = user.strip()
        user = user.lower()
        if user in badsDict:
            badsDict[user]+=1
        else:
            badsDict[user]=1
    await ctx.send(f"@{name}, you have been warned {badsDict[name]} time(s).")


@bot.command(name='commands')
async def commands(ctx):
    commandsList = ["!warn (name)","!numwarn (name)"]
    await ctx.send(commandsList)


if __name__ == "__main__":
    bot.run()