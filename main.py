import asyncio
from typing import Type

import discord
from discord.ext.commands import Cog

from src.cogs import ExampleCog
from src.core import Bot
from src.core.config import DISCORD_TOKEN


async def main():
    intents: discord.Intents = discord.Intents.default()
    intents.message_content = True
    commands: list[Type[Cog]] = [
        ExampleCog,
    ]

    async with Bot(command_prefix=">", intents=intents, custom_commands=commands) as bot:
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
