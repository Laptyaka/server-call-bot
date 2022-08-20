import discord


class Embed:
    global avatar
    avatar = "https://cdn.discordapp.com/avatars/424172023418454020/6fca84235b59a619b7d3bb2d471d2fa4.png?size=256"
    global glent
    glent = "https://i.pinimg.com/originals/df/7a/aa/df7aaaa291637eb293a401426ed6fdb2.jpg"

    def in_call(ctx, invite, icon):
        inCall = discord.Embed(
            title="Incoming call",
            description="{} is calling you!".format(ctx.author.mention),
            color=discord.Colour.green(),
            url=invite
        )
        inCall.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        inCall.set_footer(text="Made by Lapt💙💛ka", icon_url=avatar)
        inCall.set_image(url=glent)
        inCall.set_thumbnail(url=icon)
        inCall.add_field(name="Server", value=ctx.guild.name, inline=True)
        inCall.add_field(name="Channel", value=ctx.author.voice.channel.name, inline=True)
        return inCall

    def called(ctx, user):
        called = discord.Embed(
            title="Outgoing call",
            description="Calling {}...".format(user.mention),
            color=discord.Colour.blurple()
        )
        called.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        called.set_footer(text="Made by Lapt💙💛ka", icon_url="https://cdn.discordapp.com/avatars/424172023418454020/6fca84235b59a619b7d3bb2d471d2fa4.png?size=256")
        called.set_thumbnail(url="https://i.pinimg.com/originals/df/7a/aa/df7aaaa291637eb293a401426ed6fdb2.jpg")
        return called

    def noVC(ctx):
        noVC = discord.Embed(
            title="Error",
            description="Join a VC first!",
            color=discord.Colour.red()
        )
        noVC.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        noVC.set_footer(text="Made by Lapt💙💛ka", icon_url="https://cdn.discordapp.com/avatars/424172023418454020/6fca84235b59a619b7d3bb2d471d2fa4.png?size=256")
        noVC.set_image(url="https://i.imgflip.com/6pj1f0.jpg")
        return noVC
