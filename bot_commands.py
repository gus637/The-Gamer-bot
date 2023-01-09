
@bot.command(name='gameinfo', help='Gets information about a game')
async def gameinfo(ctx, *, game):
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
	message = f"Name: {name}\nRelease Date: {release_date}\nPlatforms: {platform_string}\nOverview: {overview}"
	await ctx.send(message)
