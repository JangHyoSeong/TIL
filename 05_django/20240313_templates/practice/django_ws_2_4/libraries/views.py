import requests
from django.shortcuts import render
from pprint import pprint

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = ''

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)
    # print(result)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)





def bestseller(request):

    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '20',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    # pprint(response['item'])
    for item in response['item']:
        info = {
            'title': item['title'],
            'author': item['author'],
            'pubDate': item['pubDate'],
            'isbn': item['isbn'],
            'salesPoint' : item['salesPoint'],
            'bestDuration' : item.get('bestDuration'),
        }
        result.append(info)

    context = {
        'result': result
    }
    return render(request, 'bestseller.html', context)
