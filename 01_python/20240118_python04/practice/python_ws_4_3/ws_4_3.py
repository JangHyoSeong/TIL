import requests
from pprint import pprint as print

dummy_data = []
for id in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(id)
    response = requests.get(API_URL)
    parsed_data = response.json()

    if float(parsed_data['address']['geo']['lat']) < 80 and float(parsed_data['address']['geo']['lng']) > -80:
        user_info = {
            'company' : parsed_data['company']['name'],
            'lat' : parsed_data['address']['geo']['lat'],
            'lng' : parsed_data['address']['geo']['lng'],
            'name' : parsed_data['name'],
        }
        dummy_data.append(user_info)


print(dummy_data)