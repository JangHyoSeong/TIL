import json


def max_popularity(artists):
    
    max = 0

    for artist in artists:
        artist_json = open(f'data/artists/{artist.get("id")}.json', encoding='utf-8')
        artist_temp = json.load(artist_json)

        if artist_temp.get('popularity') > max:
            max = artist_temp.get('popularity')
            popular_artist = artist
    
    return popular_artist.get('name')


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_popularity(artists_list))
