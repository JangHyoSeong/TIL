import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):

    temp_censored_user_list = dict()
    censored_user_list = dict()

    for user in user_list:
        temp_censored_user_list[user["company"]["name"]] = [user["name"]]

    for censored_user, user_name in temp_censored_user_list.items():
        # print(censored_user)
        isCensor = censorship(censored_user, user_name)
        if isCensor == True:
            censored_user_list[censored_user] = user_name

    return censored_user_list

def censorship(censored_user, censored_user_name):

    if censored_user in black_list:
        print(f'{censored_user} 소속의 {censored_user_name[0]} 은/는 등록할 수 없습니다.')
        return False
    
    else:
        print('이상 없습니다')
        return True

user_list = []

for id in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(id)
    response = requests.get(API_URL)
    parsed_data = response.json()
    user_list.append(parsed_data)

a = create_user(user_list)
print(a)