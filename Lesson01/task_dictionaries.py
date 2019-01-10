weather = {
    'city': 'Kyiv',
    'temp.': 20,
    'wind': 'east'
}

print(weather.get('city', 'Key is invalid.'))

weather['temp.'] = 23
print(weather.get('temp.', 'Key is invalid.'))

print(len(weather))

print('country' in weather)

weather['date'] = '25.07.2017'

my_list = []
my_list.append(weather)
weather['date'] = '01.10.2018'
my_list.append(weather)
weather['date'] = '31.12.2018'
my_list.append(weather)

print(my_list)
