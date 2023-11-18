# This is a sample Python script.
import os

from artbot import bot
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import discord
from dotenv import load_dotenv

load_dotenv()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # intents = discord.Intents.default()
    # intents.messages = True
    # intents.message_content = True
    # client = MyClient(command_prefix='!', intents=intents)
    # # client.add_command(client.hello)
    # # client.add_command(client.ask_command)
    bot.run(os.environ['DISCORD_TOKEN'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
