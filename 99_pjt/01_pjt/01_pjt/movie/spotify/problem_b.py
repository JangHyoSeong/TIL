import json
from pprint import pprint


def artist_info(artist, genres):

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

    return artistData


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
