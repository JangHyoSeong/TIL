import json
from pprint import pprint


def artist_info(artists, genres):

    artists_data = []

    for artist in artists:
        genreName = []
        for genre in genres:
            if genre.get('id') in artist.get('genres_ids'):
                genreName.append(genre.get('name'))
        
        artistData = {
            'id' : artist.get('id'),
            'name' : artist.get('name'),
            'genres_names' : genreName,
            'images' : artist.get('images'),
            'type' : artist.get('type'),
        }
        artists_data.append(artistData)


    return artists_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
