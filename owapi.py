import requests

player = input('Please enter your Player Name and tag like this \'example#1234\' (Caps Specific)(PC Only): \n')
region = input('Please enter your region (\'us\' \'asia\' \'eu\'): \n')
player = player.replace('#', '-')

data = requests.get(f'https://ow-api.com/v1/stats/pc/{region}/{player}/profile')
if data.status_code == 400:
    print('Player not found')
else:
    data = data.json()

    print(f"Username: {data['name']}")
    print(f"Endorsement Level: {data['endorsement']}")
    print(f"Level: {data['prestige']}{data['level']}")
    print(f"Total Games Won: {data['gamesWon']}sr")
    print(f"Tank SR: {data['ratings'][0]['level']}sr")
    print(f"Damage SR: {data['ratings'][1]['level']}sr")
    print(f"Support SR: {data['ratings'][2]['level']}sr")
