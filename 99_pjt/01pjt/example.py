import requests
import pprint


API_KEY = 'a3ae7898adbd725319711421e217fcb2'

# 서울의 위도 경도
lat = 35.1796
lon = 129.0756

URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

data = requests.get(URL).json()
#.get() : 해당 주소에서 데이터를 가져오는 함수
#.json() : 가져온 파일을 json으로 변환

pprint.pprint(data['weather'][0]['description'])    # pprint : json파일을 보기 좋게 출력함


# 날씨 API Current Weather Data로 사용해야함

# 직접 추가로 해보자
# data['weather']         # 이렇게 weather를 가져왔는데
# data.get('weather')       # 이렇게는 못쓰나? -> 된다
#차이점이 뭘까

pprint.pprint(data.get('weather'))
# 차이점
# .get은 값이 없으면 None을 반환
# 그냥 딕셔너리에서 가져오는 것은 값이 없다면 KeyError 발생
# 따라서 키가있는지 제대로 모르면 .get, 제대로 안다면 []로 가져옴
