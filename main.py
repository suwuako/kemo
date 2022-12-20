import discord

from src.read_json import read
from discord.ext import commands

class main(discord.Client):
    def __init__(self):
        self.token = read("ext/secret.json")["token"]
        @bot.event
        async def on_ready():
            print("Ready!")


    def run(self):
        bot.run(self.token)

if __name__ == "__main__":
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    main = main()
    main.run()