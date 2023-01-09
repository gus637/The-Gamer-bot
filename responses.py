import random;from resorses import games;import requests


def handle_response(message: str) -> str:
	if message == 'hello' or 'hi': return 'Hi!'

	if message[0] == "!":
		if message == '!game':
			return games[random.randint(0, len(games))]

		elif message == '!help':
			return "`commands:\n!game: returns a random game that is in a list.\n!help: returns this message.\n`"

		elif message[0:7] == 'gameinfo':
			message = message.split(" ")
			game = message[1]
			# Replace YOUR_API_KEY with your own API key
			api_key = "YOUR_API_KEY"
			headers = {
				"user-key": api_key
			}
			# Replace YOUR_ENDPOINT with the correct endpoint for the API you are using
			endpoint = "YOUR_ENDPOINT"
			params = {
				"search": game
			}
			r = requests.get(endpoint, headers=headers, params=params)
			data = r.json()

			# Extract the necessary information from the API response
			game_info = data['results'][0]
			name = game_info['name']
			release_date = game_info['released']
			platforms = game_info['platforms']
			platform_string = ", ".join([platform['name'] for platform in platforms])
			overview = game_info['overview']

			# Build the message to send to Discord
			return f"Name: {name}\nRelease Date: {release_date}\nPlatforms: {platform_string}\nOverview: {overview}"

		else:
			return "not a command"
