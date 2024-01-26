import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def ranking():
    # 여기에 코드를 작성합니다.
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
    release_list = []
    for song in result:
        release_list.append(song['album']['release_date'])
    release_list.sort(reverse=True)
    return release_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    ['2023-06-09', '2023-05-22', '2023-05-12', '2023-05-08', '2023-05-01']
    """
