import requests
from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# 변환 데이터 출력
# print(parsed_data)

dummy_data = []
for id in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(id)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])


print(dummy_data)