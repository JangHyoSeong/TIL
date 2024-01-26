import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_popular_tracks():

    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': 'genre:K-pop',  # 필수 파라미터
        'type': 'track',  # 필수 파라미터
        'market': 'KR',
        'limit': 20,
    }


    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    result = response.get('tracks').get('items')
    name_list = []
    for song in result:
        if song['popularity'] >= 90:
            name_list.append(song['name'])

    return name_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_popular_tracks())
    """
    ['Cupid - Twin Ver.', 'Take Two', 'Like Crazy', 'MONEY', 'OMG', 'Like Crazy']
    """
