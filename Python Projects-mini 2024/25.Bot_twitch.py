from twitchio.ext import commands

# Initialize the bot with necessary credentials and settings
bot = commands.Bot(
    irc_token='',         # The OAuth token for the bot (usually starts with 'oauth:')
    client_id='',         # The Twitch client ID for the bot application
    nick='',              # The username of the bot
    prefix='!',           # Command prefix used to trigger bot commands
    initial_channels=['...']  # List of channels the bot will join initially
)

@bot.event
async def event_ready():
    """
    Event handler for when the bot successfully connects and is ready.
    """
    print('Estamos listos')

@bot.command(name='horario')
async def horario(ctx):
    """
    Command handler for the 'horario' command. Responds with the bot's schedule.
    """
    await ctx.send(f'Buenas, {ctx.author.name}, mi horario es: X')

@bot.event
async def event_message(ctx):
    """
    Event handler for incoming messages. Handles commands and specific message content.
    """
    # Ensure that commands are handled
    await bot.handle_commands(ctx)
    
    # Respond to specific message content
    if 'crack' in ctx.content.lower():
        await ctx.channel.send(f'Tú sí eres un crack, {ctx.author.name}')

# Run the bot
bot.run()
