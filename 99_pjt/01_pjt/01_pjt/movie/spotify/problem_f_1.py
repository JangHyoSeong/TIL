"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():

    artist_list = []

    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)  

    for artist in artists_list:
        artist_json = open(f'data/artists/{artist.get("id")}.json', encoding='utf-8')
        artist_temp = json.load(artist_json)

        followers = artist_temp.get('followers').get('total')

        if followers < 10000000 and followers >= 5000000:
            condition_matched_artist = {
                'followers' : followers,
                'name' : artist.get('name')
            }
            artist_list.append(condition_matched_artist)
            
    return artist_list




# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
