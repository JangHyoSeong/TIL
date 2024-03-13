from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = ''
    params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'MaxResults': 50,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
    }

    response = requests.get(API_URL, params=params).json()
    context = response

    return render(request, 'index.html', context)