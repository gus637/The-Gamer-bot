import discord
from resorses import *
from discord_user import DiscordUser
import responses
from bot_bata import BUG


async def send_message(message, user_message, user, is_private):
    try:
        response = responses.handle_response(user_message, user)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        if BUG:
            print(e)


def run_discord_bot():
    from bot_bata import TOKEN, FILE_PATH
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    File.path = FILE_PATH
    File.reload()
    
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
        if user_id not in DiscordUser.users:
            # If the user is not in the dictionary, add them to the dictionary
            DiscordUser(username, user_id, new_user=True)
            file = File(DiscordUser.users[user_id])
            file.new_file()
        # Get the user from the dictionary
        user = DiscordUser.users[user_id]
        if len(message.content) > 0:
            user.messages = str(message.content)
        if user.add_xp(10):
            await message.channel.send(f"{username} has leveled up to level {user.level}")
        file = File(DiscordUser.users[user_id])
        file.save()
        username = user.name
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
        if len(user_message) != 0:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, user, is_private=True)
            else:
                await send_message(message, user_message, user, is_private=False)

    client.run(TOKEN)
