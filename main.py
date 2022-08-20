import os
import discord
from discord.ui import Button, View
from login import isHeroku
from embeds import Embed
if not isHeroku.isHeroku():
    from dotenv import load_dotenv
    load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                        name="/call"))
    print(f"{bot.user} is ready and online!")


@bot.user_command(name="Call", description="Call someone!")
@bot.slash_command(name="call", description="Call someone!")
async def call(ctx, user: discord.User):
    icon = ctx.guild.icon.url if ctx.guild.icon else ""
    if ctx.author.voice:
        invite = await ctx.author.voice.channel.create_invite(max_age=600, max_uses=1, unique=True)

        in_call = Embed.in_call(ctx, invite, icon)
        join = Button(emoji="🟢", url=f"{invite}")
        view = View()
        for _ in range(3):
            view.add_item(join)
        await user.send(view=view, embed=in_call, delete_after=600)

        called = Embed.called(ctx, user)
        await ctx.respond(embed=called, delete_after=15)
        print(ctx.author.name + " called " + user.name)
    else:
        noVC = Embed.noVC(ctx)
        await ctx.respond(embed=noVC, delete_after=10)
        print(ctx.author.name + " tried to call " + user.name
              + " but was not in a VC")

bot.run(os.environ['TOKEN'])
