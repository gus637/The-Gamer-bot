import random;from resorses import games


def handle_response(message: str, user) -> str:
	match message:
		case ('hi'):
			return 'Hi!'

		case ('!game'):
			return games[random.randint(0, len(games) - 1)]
		
		case ('!rank'):
			return f"you're level {user.level}"

		case ('!help'):
			return "`commands:\n!game: returns a random game that is in a list.\n!rank: shows your level and xp.\n!help: returns this message.\n`"

		case (_):
			if message[0] == "!":
				return "not a command"
