from discord.ext.commands import Bot, command, Context, Cog


class ExampleCog(Cog):
    path: str = __name__

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="meow")
    async def meow(self, context: Context):
        await context.message.reply("Nya~")


async def setup(bot: Bot):
    await bot.add_cog(ExampleCog(bot))
