weather_kyiv = {
	'city': 'Kyiv',
	'temperature': -5,
	'wind': 'north-west'
}

weather_vinnica = {
	'city': 'Vinnica',
	'temperature': -10,
	'wind': 'north'
}

weather_lviv = {
    'city': 'Lviv',
    'temperature': 2,
    'wind': 'south'
}


people = {
	'Vova': weather_vinnica,
	'Lena': weather_kyiv,
	'Polina': weather_lviv
}


value = input('Enter name: ').capitalize()
value2 = people.get(value, 'Enter correct value')
print('{}: {}'.format(value, value2))
