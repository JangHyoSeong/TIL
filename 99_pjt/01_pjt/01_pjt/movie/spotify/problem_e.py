import json


def dec_artists(artists):

    artists_list = []

    for artist in artists:
        artist_json = open(f'data/artists/{artist.get("id")}.json', encoding='utf-8')
        artist_temp = json.load(artist_json)
        
        if artist_temp.get('followers').get('total') >= 10000000:
            
            url_split = artist_temp.get('uri').split(':')
            artist_url = url_split[2]
            popular_artist = {
                'name' : artist_temp.get('name'),
                'uri-id' : artist_url,
            }
            artists_list.append(popular_artist)

    return artists_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
