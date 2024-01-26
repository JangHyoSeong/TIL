import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'track:{track}',  # 필수 파라미터
        'type': 'track',  # 필수 파라미터
        'market': 'KR',
        'limit': 20,
    }

    response_track = requests.get(f'{URL}/search', headers=headers, params=params)
    response_track = response_track.json()
    track_id = response_track['tracks']['items'][0]['id']
    

    params = {
        'q': f'artist:{artist}',  # 필수 파라미터
        'type': 'artist',  # 필수 파라미터
        'market': 'KR',
        'limit': 20,
    }

    response_artist = requests.get(f'{URL}/search', headers=headers, params=params)
    response_artist = response_artist.json()

    artist_id = response_artist['artists']['items'][0]['id']

    params = {
        'seed_artists' : artist_id,
        'seed_genres' : genre,
        'seed_trakcs' : track_id,
        'limit' : 10,
        'market' : 'KR'
    }

    response_recommended = requests.get(f'{URL}/recommendations', headers=headers, params=params)
    response_recommended = response_recommended.json()

    recommended = []
    song_list = response_recommended['tracks']
    for song in song_list:
        recommended.append(song['name'])

    return recommended

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
