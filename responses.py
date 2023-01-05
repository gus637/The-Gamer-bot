import random
from resorses import games


def handle_response(message: str) -> str:
    message.lower()

    if message == 'hello': return 'Hi!'

    if message[0] == "!":
        if message == '!game': return games[random.randint(0, len(games))]

        elif message == '!help': return "`commands:\n!game: returns a random game that is in a list.\n!help: returns this message.\n`"

        else: return "not a command"
