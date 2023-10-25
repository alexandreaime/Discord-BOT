from discord.ext import commands
import discord
import random
from credentials import TOKEN_DISCORD

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 258662962921865218  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.message.author)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1, 6))

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send(f"Salut tout seul {message.author.mention}")
    else:
        await bot.process_commands(message)

@bot.command()
async def admin(ctx, member: discord.Member):
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    if not admin_role:
        admin_role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions.all())
        for channel in ctx.guild.channels:
            await channel.set_permissions(admin_role, read_messages=True, send_messages=True)
    else:
        await member.add_roles(admin_role)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=""):
    if not reason:
        funny_catchphrases = [
            "banni pour sauvagerie",
            "banni pour c'est mieux pour toi tkt",
            "banni pour avoir supporté l'OM",
            "banni pour préférer One Piece à Naruto",
        ]
        reason = random.choice(funny_catchphrases)
    await member.ban(reason=reason)
    await ctx.send(f"{member} a été {reason}")

bot.run(TOKEN_DISCORD)  # Starts the bot