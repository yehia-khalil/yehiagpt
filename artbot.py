import discord
from discord.ext import commands
from openAi import OpenAiClient
from chunkMessage import split_message

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
gpt = OpenAiClient()

# Initialize Discord bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
mapper = {}
context_size = 10
ignore_list = ["!showcontext", "!clearcontext", "!usecontext"]


# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


# Command to respond with "Hello"
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send("Hello")


# Command to use OpenAI
@bot.command(name='ask')
async def ask_command(ctx, *, query: str = ""):
    if len(query) == 0:
        await ctx.send("Please provide a query")

    gpt_response = await gpt.ask_gpt(query)
    response_chunks = split_message(gpt_response)

    # Send each chunk as a separate message
    for chunk in response_chunks:
        await ctx.send(chunk)


@bot.command(name='setcontext')
async def setcontext(ctx, *, query: str = ""):
    global context_size  # Declare that we're using the global variable
    try:
        context_size = int(query)  # Convert the input to an integer
        await ctx.send(f"Context size set to {context_size}")
    except ValueError:
        await ctx.send("Please enter a valid integer for the context size.")


@bot.command(name='showcontext')
async def show_context(ctx):
    if context_size == 0:
        await ctx.send(
            "Set context messages count before using context. You can use the `!setcontext` command to do so.")
    await ctx.send("\n".join(item for item in mapper[ctx.channel.id]))


@bot.command(name='clearcontext')
async def clear_context(ctx):
    if context_size == 0:
        await ctx.send(
            "Set context messages count before using context. You can use the `!setcontext` command to do so.")
    mapper[ctx.channel.id] = []
    await ctx.send("Context cleared successfully.")


@bot.command(name='usecontext')
async def use_context(ctx, *, query: str):
    context = "\n".join(item for item in mapper[ctx.channel.id])
    if query:
        query = context + query
    else:
        query = context
    gpt_response = await gpt.ask_gpt(query)
    response_chunks = split_message(gpt_response)

    # Send each chunk as a separate message
    for chunk in response_chunks:
        await ctx.send(chunk)


# Event handler for processing messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if context_size != 0:
        await add_to_context(message)

    await message.channel.typing()
    await bot.process_commands(message)


async def add_to_context(message):
    if message.content != "" and message.content not in ignore_list:
        if mapper.get(message.channel.id) is not None:
            if len(mapper[message.channel.id]) > context_size:
                mapper[message.channel.id].pop(0)
            mapper[message.channel.id].append(f"{message.author} : {message.content}")
        else:
            mapper[message.channel.id] = []
            mapper[message.channel.id].append(f"{message.author} : {message.content}")
