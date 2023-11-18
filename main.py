# This is a sample Python script.
import os

from dotenv import load_dotenv
from gpt import bot
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.run(os.environ['DISCORD_TOKEN'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
