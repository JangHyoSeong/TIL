import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    params = {
        'q': f'artist:{name}',  # 필수 파라미터
        'type': 'artist',  # 필수 파라미터
        'market': 'KR',
        'limit': 20,
    }


    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    artist = response.get('artists').get('items')
    for singer in artist:
        if singer['name'] == name:
            id = singer['id']

    try:
        URL = f'https://api.spotify.com/v1/artists/{id}/related-artists'
    except:
        return None
    response = requests.get(f'{URL}', headers=headers)
    response = response.json()

    related_artist = response['artists']

    related_list = []
    for relate in related_artist:
        related_list.append(relate['name'])

    return related_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    print(get_related_artists("NewJeans"))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists("OldShirts"))
    # None
