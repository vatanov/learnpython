user_info = {'first_name': '', 'last_name': ''}

user_info['first_name'] = input('Enter your name: ').capitalize()
user_info['last_name'] = input('Enter your surname: ').capitalize()

print('Your full name is {} {}'.format(user_info['first_name'], user_info['last_name']))
