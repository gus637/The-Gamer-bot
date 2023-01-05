import discord
import responses
from discord_user import DiscordUser, users



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    from bot_bata import TOKEN
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is online!')

    @client.event
    async def on_message(message):
        # Check if the message is from a bot
        if message.author.bot: return
        # Get the user's name and ID
        username = message.author.name
        user_id = message.author.id

        # Check if the user is in the dictionary
        if user_id not in users:
            # If the user is not in the dictionary, add them to the dictionary
            users[user_id] = DiscordUser(username, user_id)
        # Get the user from the dictionary
        user = users[user_id]
        user.add_xp(10)

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
